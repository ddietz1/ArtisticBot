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
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hexagon.png')
        image = cv2.imread(img_path)
        h, w = image.shape[:2]

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # threshold instead of Canny — more reliable for simple shapes
        _, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # filter out contours that are too large (image border)
        contours = [c for c in contours if cv2.contourArea(c) < 0.9 * w * h]
        
        # pick largest remaining
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
        if not contours:
            self.get_logger().error('No valid contours found')
            return None

        epsilon = 0.02 * cv2.arcLength(contours[0], True)
        approx = cv2.approxPolyDP(contours[0], epsilon, closed=True)

        coords = [(pt[0][0] / w, pt[0][1] / h) for pt in approx]
        self.get_logger().info(f'Detected {len(coords)} vertices: {coords}')
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
