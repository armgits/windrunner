#!/bin/bash
source /opt/ros/noetic/setup.bash

cd ~/catkin_ws && catkin_make
source devel/setup.bash

sudo pip3 install pyyaml

git clone https://github.com/armgits/windrunner.git ~/catkin_ws/src/windrunner_project

sudo rm -rf ~/cakin_ws/src/windrunner_project/cad/ \
  ~/cakin_ws/src/windrunner_project/dockerfile/ \
  ~/cakin_ws/src/windrunner_project/image/ \
  ~/cakin_ws/src/windrunner_project/README.md

sudo chmod +x ~/catkin_ws/src/windrunner_project/windrunner/src/windrunner_publisher.py
sudo chmod +x ~/catkin_ws/src/windrunner_project/windrunner/src/windrunner_teleop.py

cd ~/catkin_ws
catkin_make clean && catkin_make
source ~/catkin_ws/devel/setup.bash
