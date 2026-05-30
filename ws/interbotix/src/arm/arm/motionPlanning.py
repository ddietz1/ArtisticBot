import rclpy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.node import Node

from scipy.spatial.transform import Rotation as R

from std_srvs.srv import Empty

from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion, Transform

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

import numpy as np

class MotionPlanning:
    """Motion Planning Node."""

    def __init__(self, bot: InterbotixManipulatorXS):
        self.node = bot.core.robot_node
        # global variables
        self.moving = False

        self.bot = bot

        # self.bot.arm.set_ee_pose_components(x=0.3, y=0.0, z=0.1)

        # Add Timers
        # To test, we will subscribe to a coordinate topic like Point or PoseStamped and move the arm to the first point

        # Create subscribers
        self.node.create_subscription(
            Pose,
            '/vision/coordinate',
            self.coordinate_cb,
            10
        )

        self.timer = self.node.create_timer(
            0.5,
            self.timer_cb
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

    def coordinate_cb(self, msg: Pose):
        """Takes in coordinates from the vision pipeline and stores them."""

        # if msg.orientation:
        #     self.move_arm(coordinate=msg, translate_only=False)
        # else:
        #     self.move_arm(coordinate=msg, translate_only=True)
        self.node.get_logger().info('Received coordinate!')
        self.move_arm(coordinate=msg)

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




