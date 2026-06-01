from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    xsarm = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('interbotix_xsarm_control'),
            '/launch/xsarm_control.launch.py'
        ]),
        launch_arguments={
            'robot_model': 'wx200', #'px100',
            'use_sim': 'false',
        }.items()
    )

    arm_coordinator = Node(
        package='arm',
        executable='arm_coordinator',
    )

    vision_node = Node(
        package='arm',
        executable='vision_node',
    )

    return LaunchDescription([xsarm, arm_coordinator, vision_node])