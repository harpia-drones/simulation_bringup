from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # # Caminho para o launch do realsense
    # realsense_launch = os.path.join(
    #     get_package_share_directory('realsense2_camera'),
    #     'launch',
    #     'rs_launch.py'
    # )

    # # Node que converte odometria do SLAM para PX4 (via MAVROS)
    # odom_to_mavros_node = Node(
    #     package='drone_slam',
    #     executable='odom_to_mavros',  # script que vamos criar (publica VISION_POSITION_ESTIMATE)
    #     output='screen'
    # )

    # RTAB-Map (RGB-D + IMU)
    rtabmap_node = Node(
        package='rtabmap_ros',
        executable='rtabmap',
        name='rtabmap',
        output='screen',
        parameters=[{
            'frame_id': 'base_link',
            'subscribe_depth': True,
            'subscribe_rgb': True,
            'subscribe_imu': True,
            'approx_sync': True,
            'wait_for_transform': 0.2,
            'use_action_for_goal': True,
            'odom_frame_id': 'odom'
        }],
        remappings=[
            ('rgb/image', '/camera/color/image_raw'),
            ('depth/image', '/camera/depth/image_rect_raw'),
            ('rgb/camera_info', '/camera/color/camera_info'),
            ('imu', '/camera/imu'),
            ('odom', '/rtabmap/odom')
        ]
    )

    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(realsense_launch),
        #     launch_arguments={'align_depth': 'true'}.items()
        # ),
        rtabmap_node,
        # odom_to_mavros_node
    ])
