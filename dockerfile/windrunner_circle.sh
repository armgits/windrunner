#!/bin/bash

cd ~/catkin_ws
source devel/setup.bash

roscore &
sleep 3
roslaunch windrunner windrunner_empty_world.launch &
sleep 3
rosrun windrunner windrunner_publisher.py &

wait -n
exit $?