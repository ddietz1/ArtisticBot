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
            'robot_model': 'px100',
            'use_sim': 'true',
        }.items()
    )

    motion_planner = Node(
        package='arm',
        executable='motion_planner',
    )

    return LaunchDescription([xsarm, motion_planner])