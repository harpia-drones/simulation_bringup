#!/root/harpia_venv/bin/python3

import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    """ This function starts the system in a custom configuration """

    # Generate the object that must be returned by this function
    ld = LaunchDescription()

    ##################################################
    #  Mount the path to the files that will be used      
    ##################################################

    ################# GZ BRIDGE ################
    gz_config_path = os.path.join(
        get_package_share_directory(f'simulation_bringup'),
        'config',
        'ros_gz_bridge',
        'bridge_param.yaml',
    )

    # gz_config_path_2 = os.path.join(
    #     get_package_share_directory(f'simulation_bringup'),
    #     'config',
    #     'ros_gz_bridge',
    #     'cameras_2.yaml'
    # )


    ##################################################
    #  Initalize simulation      
    ##################################################

    ################# GZ BRIDGE ################
    ros_gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{'config_file': gz_config_path}],
        output='screen'
    )

    # ros_gz_bridge_node_2 = Node(
    #     package='ros_gz_bridge',
    #     executable='parameter_bridge',
    #     parameters=[{'config_file': gz_config_path_2}],
    #     output='screen'
    # )

    ##################################################
    #  Add the action to LaunchDescription object 
    ##################################################

    ld.add_action(ros_gz_bridge_node)
    # ld.add_action(ros_gz_bridge_node_2)

    return ld