# simulation_bringup

ROS 2 package that starts the full simulation stack for the Harpia drone setup.

## Overview

This package centralizes the simulation startup flow in a single launch entry point. It runs a shared shell script that brings up the main components needed for SITL testing:

- MicroXRCEAgent
- PX4 SITL with Gazebo
- QGroundControl
- ROS/Gazebo bridge

## Launch

```bash
ros2 launch simulation_bringup simulation.launch.py
```

This starts a tmux session named `HarpiaSim` with separate windows for the simulation essentials and supporting tools.
