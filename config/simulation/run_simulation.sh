#!/usr/bin/env bash

# USAGE:
#   ./script.sh [PX4_GZ_WORLD]
#
# ARGUMENTS:
#   PX4_GZ_WORLD : Name of the Gazebo world to launch (Optional. Defaults to "default")

WORLD="${1:-default}"

# Tmux session and window names
SESSION="HarpiaSim"
WINDOW_0="main"
WINDOW_1="sim-essentials"
WINDOW_2="sim-tools"

# Commands to run in each pane
START_MICROXRCE_AGENT="MicroXRCEAgent udp4 -p 8888"
START_QGC='runuser -l harpia -c "DISPLAY=${DISPLAY} /usr/local/bin/QGroundControl"'
START_PX4='cd /root/PX4-Autopilot && PX4_GZ_WORLD=$WORLD make px4_sitl gz_harpia'
START_BRIDGE="ros2 launch simulation_bringup ros_gz_bridge.launch.py"


if [ -n "$TMUX" ]; then    # Check if the script is running inside a tmux session
    SESSION=$(tmux display-message -p '#S')
    tmux new-window -d -t $SESSION -n $WINDOW_0

elif tmux has-session -t $SESSION 2>/dev/null; then    # Check if a tmux session with default name exists
    echo "Session $SESSION already exists. Attaching to it..."
    tmux attach-session -t $SESSION
    exit 0

else    # Create new session
    tmux new-session -d -s $SESSION: -n $WINDOW_0
fi

# Set up the windows inside the session
tmux new-window -d -t $SESSION: -n $WINDOW_1
tmux new-window -d -t $SESSION: -n $WINDOW_2

# Set up the sim-essentials window with a tiled layout
tmux split-window -h -t $SESSION:$WINDOW_1
tmux split-window -v -t $SESSION:$WINDOW_1.0
tmux split-window -v -t $SESSION:$WINDOW_1.2
tmux select-layout -t $SESSION:$WINDOW_1 tiled

# Send commands to the respective panes in the sim-essentials window
tmux send-keys -t $SESSION:$WINDOW_1.0 "$START_MICROXRCE_AGENT" C-m
tmux send-keys -t $SESSION:$WINDOW_1.1 "$START_PX4" C-m
tmux send-keys -t $SESSION:$WINDOW_1.2 "$START_QGC" C-m
tmux send-keys -t $SESSION:$WINDOW_1.3 "$START_BRIDGE" C-m

#Attach to the session
tmux select-window -t $SESSION:$WINDOW_0
tmux attach-session -t $SESSION
