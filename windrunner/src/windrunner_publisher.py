#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64


def MoveCommand():
    rospy.init_node('teleop')

    pub_right = rospy.Publisher('/windrunner/right_steering_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left = rospy.Publisher('/windrunner/left_steering_controller/command', Float64, queue_size=10)
    pub_rear_right = rospy.Publisher('/windrunner/rear_right_wheel_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    pub_rear_left = rospy.Publisher('/windrunner/rear_left_wheel_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(10)

    control_turn = 1
    control_speed = 10

    while not rospy.is_shutdown():
        pub_right.publish(-control_turn) # publish the turn command.
        pub_left.publish(-control_turn) # publish the turn command.
        pub_rear_right.publish(-control_speed) # publish the control speed. 
        pub_rear_left.publish(-control_speed)
        rospy.loginfo("Turning Right: %s",control_turn)
        rospy.loginfo("Turning Left: %s",control_turn)
        rospy.loginfo("Speed: %s",control_speed)
        
        rate.sleep()

if __name__=="__main__":
    try:
        MoveCommand()
    except rospy.ROSInterruptException:
        pass