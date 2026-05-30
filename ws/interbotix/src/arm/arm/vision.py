"""Vision Pipeline"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
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

        # run detection once on init and publish
        coords = self.detect_coords()
        if coords is not None:
            self.publish_coords(coords)

    def detect_coords(self):
        image = cv2.imread("triangle.png")
        if image is None:
            self.get_logger().error("Could not load triangle.png")
            return None

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img_gray, 30, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if not contours:
            self.get_logger().error("No contours found")
            return None

        approx = cv2.approxPolyDP(contours[0], 0.01 * cv2.arcLength(contours[0], True), closed=True)
        self.get_logger().info(f'Found {len(approx)} points')
        return approx.reshape(-1, 2)  # flatten to list of (u, v)

    def publish_coords(self, coords):
        points = []

        # normalize coordinates
        img_w = 640
        img_h = 480

        for c in coords:
            u = c[0] / img_w
            v = c[1] / img_h
            p = Point()
            p.x = float(u)
            p.y = float(v)
            p.z = 0.0

            points.append(p)
        msg = Pixels()
        msg.points = points
        self.pub.publish(msg)
        self.get_logger().info(f'Published {len(points)} points')

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

# cv2.imshow('Canny Edges after contouring', edges)

# cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
# cv2.imshow('Contours', image)

# cv2.drawContours(image, approx, -1, (0, 0, 255), 3)
# cv2.imshow('Contours(approx)', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()