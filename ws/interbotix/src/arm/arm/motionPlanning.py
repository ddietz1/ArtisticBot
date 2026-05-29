import rclpy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.node import Node

from scipy.spatial.transform import Rotation as R

from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion, Transform

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

class MotionPlanning:
    """Motion Planning Node."""

    def __init__(self, bot: InterbotixManipulatorXS):
        self.node = bot.core.robot_node
        # global variables
        self.moving = False

        self.bot = bot

        self.bot.arm.set_ee_pose_components(x=0.3, y=0.0, z=0.1)

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

    def timer_cb(self):
        """Timer."""

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


def main(args=None):
    rclpy.init(args=args)
    bot = InterbotixManipulatorXS("px100", "arm", "gripper")
    mp = MotionPlanning(bot)
    rclpy.spin(bot.core.robot_node)
    rclpy.shutdown()




