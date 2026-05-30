import rclpy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.node import Node

from scipy.spatial.transform import Rotation as R

from std_srvs.srv import Empty

from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion, Transform

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

import numpy as np

from collections import deque

from arm_interfaces.msg import Pixels

class MotionPlanning:
    """Motion Planning Node."""

    def __init__(self, bot: InterbotixManipulatorXS):
        self.node = bot.core.robot_node
        # global variables

        # workspace bounds
        self.x_min, self.x_max = 0.15, 0.35
        self.y_min, self.y_max = -0.15, 0.15
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

        # from vision pipeline
        self.node.create_subscription(
            Point,
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

        # if empty just return
        if not self.point_queue:
            self.moving = False
            return
        
        p = self.point_queue.popleft()
        x, y = self.pixel_to_robot(p.x, p.y)

        self.node.get_logger(f"sending robot to point: x={x:.3f}, y={y:.3f}")
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
        x = self.x_max - v * (self.x_max - self.x_min)
        y = self.y_max - u * (self.y_max - self.y_min) * 2

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
    rclpy.init(args=args)
    bot = InterbotixManipulatorXS("px100", "arm", "gripper")
    mp = MotionPlanning(bot)
    rclpy.spin(bot.core.robot_node)
    rclpy.shutdown()




