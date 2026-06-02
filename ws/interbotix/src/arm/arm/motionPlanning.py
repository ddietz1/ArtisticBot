import rclpy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.node import Node

import time

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

        # workspace bounds for pincherx
        # self.x_min, self.x_max = 0.17, 0.27
        # self.y_min, self.y_max = -0.15, 0.15

        # workspace bounds for wx200
        self.x_min, self.x_max = 0.28, 0.43  
        self.y_min, self.y_max = -0.15, 0.15
        self.z = 0.1          
        self.node.declare_parameter('z_travel', 0.15)
        self.node.declare_parameter('z_draw', 0.088)
        self.moving = False

        self.bot = bot

        self.point_queue = deque()

        self.drawing_group = MutuallyExclusiveCallbackGroup()

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
            self.queue_cb,
            callback_group=self.drawing_group
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

        # update z value parameters
        self.z_travel = self.node.get_parameter('z_travel').get_parameter_value().double_value
        self.z_draw = self.node.get_parameter('z_draw').get_parameter_value().double_value

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

        # down_pitch = np.pi/2 

        success = self.bot.arm.set_ee_pose_components(x=x, y=y, z=self.z_travel)
        
        if success:
            self.bot.arm.set_ee_pose_components(x=x, y=y, z=self.z_draw)
            self.bot.arm.set_ee_pose_components(x=x, y=y, z=self.z_travel)
        else:
            self.node.get_logger().warn(f"Point out of reach! Skipping x={x:.3f}, y={y:.3f}")

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
        self.node.get_logger().info(f'Moving to x={x}, y={y}, z={z}') 

        if translate_only:
            self.bot.arm.set_ee_pose_components(x=x, y=y, z=z)

    def pixel_to_robot(self, u, v):
        """Transform pixels from vision pipeline to robot coordinates."""

        ws_x_span = self.x_max - self.x_min
        ws_y_span = self.y_max - self.y_min

        draw_size = min(ws_x_span, ws_y_span)

        x_center = (self.x_min + self.x_max) / 2.0
        y_center = (self.y_min + self.y_max) / 2.0

        x = x_center + (0.5 - v) * draw_size
        y = y_center + (0.5 - u) * draw_size

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
        robot_model="wx200",#"px100",
        group_name="arm",
        gripper_name="gripper",
        moving_time=1.6,
        accel_time=0.1,
        gripper_pressure=1.0, 
        node=global_node,
    )

    # Create your class, attach subscriptions/services to global_node
    mp = MotionPlanning(bot)
        # pixels arrive normalized
        # x = self.x_min + (1.0 - v) * (self.x_max - self.x_min)
        # y = self.y_min + (1.0 - u) * (self.y_max - self.y_min)
    # Start the executor — callbacks fire from here
    robot_startup(global_node)

    try:
        while rclpy.ok():
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        robot_shutdown(global_node)




