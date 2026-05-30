import rclpy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.node import Node

from scipy.spatial.transform import Rotation as R

from std_srvs.srv import Empty

from geometry_msgs.msg import Point, Pose, PoseStamped, PolygonStamped
from nav_msgs.msg import Path
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

import numpy as np

from collections import deque

from arm_interfaces.msg import Pixels

from interbotix_common_modules.common_robot.robot import (
    create_interbotix_global_node,
    robot_startup,
    robot_shutdown
)

class MotionPlanning:
    """Motion Planning Node."""

    def __init__(self, bot: InterbotixManipulatorXS):
        self.node = bot.core.robot_node
        # global variables

        # workspace bounds
        self.x_min, self.x_max = 0.20, 0.26
        self.y_min, self.y_max = -0.06, 0.06
        self.z = 0.1                    # fixed for now
        self.moving = False

        self.bot = bot

        self.point_queue = deque()

        # self.bot.arm.set_ee_pose_components(x=0.3, y=0.0, z=0.1)

        # Add Timers
        # To test, we will subscribe to a coordinate topic like Point or PoseStamped and move the arm to the first point

        # Create subscribers

        # for testing
        self.node.create_subscription(
            Pose,
            '/vision/coordinate',
            self.coordinate_cb,
            10
        )

        self.display_pub = self.node.create_publisher(
            Path,
            '/shape_visual',
            10
        )

        # from vision pipeline
        self.node.create_subscription(
            Pixels,
            '/vision/points',
            self.pixel_cb,
            10               # probably fix this, reliable?
        )

        self.timer = self.node.create_timer(
            0.5,
            self.timer_cb
        )

        self.point_timer = self.node.create_timer(
            2.5,
            self.queue_cb
        )

        # Create services
        self.close_grip = self.node.create_service(
            Empty,
            'gripper/close',
            self.close_gripper
        )

        self.open_grip = self.node.create_service(
            Empty,
            'gripper/open',
            self.open_gripper
        )

        self.sleep = self.node.create_service(
            Empty,
            'sleep',
            self.sleep
        )

        self.pen = self.node.create_service(
            Empty,
            'pen',
            self.align_pen
        )

    def timer_cb(self):
        """Timer."""

        # Go to home pose once
        self.bot.arm.go_to_home_pose()
        self.timer.cancel()

    def queue_cb(self):
        """Processes points from the vision pipeline."""

        now = self.node.get_clock().now().to_msg()
        # if empty just return
        if not self.point_queue:
            self.moving = False
            return
        
        # draw the shape in rviz
        polygon_points = []
        for p in self.point_queue:
            # make each a pose stamped
            pose = PoseStamped()
            x, y = self.pixel_to_robot(p.x, p.y)
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.position.z = 0.1
            pose.pose.orientation.w = 1.0
            pose.header.frame_id =  'px100/base_link'
            pose.header.stamp = now
            polygon_points.append(pose)

        poly = Path()
        poly.poses = polygon_points
        poly.header.frame_id =  'px100/base_link'
        poly.header.stamp = now
        self.display_pub.publish(poly)

        p = self.point_queue.popleft()
        self.node.get_logger().info(f"point in the queue: x={p.x}, y={p.y}")
        x, y = self.pixel_to_robot(p.x, p.y)

        self.node.get_logger().info(f"sending robot to point: x={x:.3f}, y={y:.3f}")
        self.bot.arm.set_ee_pose_components(x=x, y=y, z=0.1)
        self.moving = True

    def coordinate_cb(self, msg: Pose):
        """Takes in coordinates from the vision pipeline and stores them."""

        self.node.get_logger().info('Received coordinate!')
        self.move_arm(coordinate=msg)

    def pixel_cb(self, msg: Pixels):
        """Recieved points from the vision pipeline."""

        self.point_queue.clear()
        # pixels is a list of points
        for p in msg.points:
            self.point_queue.append(p)
        self.node.get_logger().info(f'Queued {len(self.point_queue)} points')


    def move_arm(self, coordinate: Pose, translate_only=True):
        """Moves the arm to a specified coordinate
        
        Parameters:
        coordinate - Pose to move the arm to
        translate_only - Determines if the arm should move with our without quaternion

        returns: None.
        """

        # deconstruct the pose components
        x = coordinate.position.x
        y = coordinate.position.y
        z = coordinate.position.z
        q = coordinate.orientation
        self.node.get_logger().info(f'Moving to x={x}, y={y}, z={z}')  # add this

        if translate_only:
            self.bot.arm.set_ee_pose_components(x=x, y=y, z=z)

    def pixel_to_robot(self, u, v):
        """Transform pixels from vision pipeline to robot coordinates."""

        # pixels arrive normalized
        x = self.x_min + (1.0 - v) * (self.x_max - self.x_min)
        y = self.y_min + (1.0 - u) * (self.y_max - self.y_min)

        return x, y

    def open_gripper(self, request, response):
        """close the gripper."""

        self.bot.gripper.grasp()
        return response

    def close_gripper(self, request, response):
        """Open the gripper."""

        self.bot.gripper.release()
        return response

    def sleep(self, request, response):
        """go to sleep pose."""

        self.bot.arm.go_to_sleep_pose()
        return response
    
    def align_pen(self, request, response):
        """Move the arm to align the pen with the page."""

        # move the wrist angle such that its pointed downward
        self.bot.arm.set_single_joint_position(
            'wrist_angle',
            np.pi/2
        )
        return response

def main(args=None):
    # Create global node first
    global_node = create_interbotix_global_node()

    # Pass it to the bot
    bot = InterbotixManipulatorXS(
        robot_model="px100",
        group_name="arm",
        gripper_name="gripper",
        node=global_node,
    )

    # Create your class, attach subscriptions/services to global_node
    mp = MotionPlanning(bot)

    # Start the executor — callbacks fire from here
    robot_startup(global_node)

    try:
        while rclpy.ok():
            pass
    except KeyboardInterrupt:
        pass
    finally:
        robot_shutdown(global_node)




