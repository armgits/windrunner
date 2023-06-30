#!/bin/bash

cd ~/catkin_ws
source devel/setup.bash

roscore &
sleep 3
roslaunch windrunner windrunner.launch &
# sleep 3
# rosrun windrunner windrunner_teleop.py &

wait -n
exit $?