"""Vision Pipeline"""

import rclpy
import os
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_srvs.srv import Empty
import cv2
import numpy as np

from arm_interfaces.msg import Pixels

class VisionNode(Node):
    def __init__(self):
        super().__init__("VisionNode")

        # create publishers
        self.pub = self.create_publisher(
            Pixels,
            '/vision/points',
            10
        )

        # create services
        self.draw = self.create_service(
            Empty,
            'draw',
            self.draw_shape
        )

    def detect_coords(self):
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'smiley_face.png')
        image = cv2.imread(img_path)
        h, w = image.shape[:2]

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # threshold instead of Canny — more reliable for simple shapes
        _, thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)

        # Skeletonization (Crush lines to 1 pixel wide)
        skeleton = cv2.ximgproc.thinning(thresh)
        
        contours, _ = cv2.findContours(skeleton, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        
        # Simplify the paths (Reduce the dots)
        dot_spacing = 1 # This is the min distance between points in the final path.
        target_dot_count = 200
        total_dots = float('inf')
        
        # Loop through contours and keep only every nth point until there are a 
        # resonable number of points for the robot to draw
        while total_dots > target_dot_count:
            robot_paths = []

            for contour in contours:
                # Filter out tiny specks so the robot doesn't draw random dots
                if len(contour) > dot_spacing: 
                    spaced_points = contour[::dot_spacing]  # Take every nth point
                    robot_paths.append(spaced_points)

            total_dots = sum(len(path) for path in robot_paths)
            if total_dots > target_dot_count:
                dot_spacing += 1 

        # Create a blank black canvas to preview the robot's paths
        preview = np.zeros_like(image)
        coords = []

        max_dim = max(w, h)
        x_offset = (max_dim - w) / 2.0
        y_offset = (max_dim - h) / 2.0

        for dot_path in robot_paths:
            for point in dot_path:
                x, y = point[0]
                # Draw green dots for the robot to follow
                cv2.circle(preview, (x, y), 3, (0, 255, 0), -1)

                # Normalize the coordinates 
                u = (float(x) + x_offset) / max_dim
                v = (float(y) + y_offset) / max_dim
                coords.append((u, v))
        cv2.imshow('Dots', preview)
        cv2.waitKey(0) 

        self.get_logger().info(f'Detected {len(coords)} vertices: {coords}')
        if coords:
            coords.append(coords[0])  # close the shape
        return coords

    def publish_coords(self, coords):
        points = []

        for c in coords:
            u = c[0]
            v = c[1]
            p = Point()
            p.x = float(u)
            p.y = float(v)
            p.z = 0.0

            points.append(p)
        msg = Pixels()
        msg.points = points
        self.pub.publish(msg)
        self.get_logger().info(f'Published {len(points)} points')

    def draw_shape(self, request, response):
        """detect and publish shape coordinates."""

        # run detection once on init and publish
        coords = self.detect_coords()

        if coords is not None:
            self.publish_coords(coords)
        else:
            self.get_logger().info('No Coordinates to publish')

        return response

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
