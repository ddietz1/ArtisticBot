"""Vision Pipeline"""

import rclpy
import os
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_srvs.srv import Empty
import cv2
import numpy as np
import math

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
        robot_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'smiley_face.png')

        image = cv2.imread(img_path)
        robot_image = cv2.imread(robot_img_path)
        h, w = image.shape[:2]

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # threshold instead of Canny — more reliable for simple shapes
        _, thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)

        # Add border to prevent edge artifacts during skeletonization
        thresh = cv2.copyMakeBorder(thresh, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)

        # Skeletonization (Crush lines to 1 pixel wide)
        skeleton = cv2.ximgproc.thinning(thresh)
        
        y_coords, x_coords = np.where(skeleton > 0)
        unvisited_points = list(zip(x_coords, y_coords))

        robot_paths = []
        current_path = []

        # TUNING PARAMETERS 
        target_spacing = 20.0  # Physical distance between dots (in pixels)
        pen_up_distance = 30.0 # If the next dot is this far away, start a new path
        
        if unvisited_points:
            current_point = unvisited_points.pop(0)
            current_path.append(current_point)

            while unvisited_points:
                pts_array = np.array(unvisited_points)
                curr_array = np.array(current_point)
                
                distances = np.linalg.norm(pts_array - curr_array, axis=1)
                
                closest_idx = np.argmin(distances)
                closest_dist = distances[closest_idx]
                closest_point = unvisited_points[closest_idx]

                if closest_dist > pen_up_distance:
                    robot_paths.append(current_path) 
                    current_path = []                
                    current_point = unvisited_points.pop(closest_idx)
                    current_path.append(current_point)
                    continue

                if closest_dist >= target_spacing:
                    current_path.append(closest_point)
                    current_point = unvisited_points.pop(closest_idx) 
                else:
                    unvisited_points.pop(closest_idx)

            if current_path:
                robot_paths.append(current_path)

        # Create a blank black canvas to preview the robot's paths
        preview = np.zeros_like(image)
        coords = []

        max_dim = max(w, h)
        x_offset = (max_dim - w) / 2.0
        y_offset = (max_dim - h) / 2.0

        for dot_path in robot_paths:
            for point in dot_path:
                x, y = point
                
                # Draw green dots for the robot to follow
                cv2.circle(preview, (x, y), 3, (0, 255, 0), -1)

                # Normalize the coordinates 
                u = (float(x) + x_offset) / max_dim
                v = (float(y) + y_offset) / max_dim
                coords.append((u, v))
                
        cv2.imshow('Dots', preview)

        # compare preview dots image with the final output from the robot

        cv2.waitKey(0) 

        self.get_logger().info(f'Detected {len(coords)} vertices')
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
