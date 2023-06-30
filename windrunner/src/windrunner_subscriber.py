#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callback_left(data):
    rospy.loginfo("Current left steering: %s", abs(data.data))

def callback_right(data):
    rospy.loginfo("Current right steering: %s", abs(data.data))
    
def callback_rear(data):
    rospy.loginfo("Current rear speed: %s", abs(data.data))
    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/windrunner/right_steering_controller/command", Float64, callback_left)
    rospy.Subscriber("/windrunner/left_steering_controller/command", Float64, callback_right)
    rospy.Subscriber("/windrunner/right_left_wheel_controller/command", Float64, callback_rear)
    rospy.spin()

if __name__ == '__main__':
    listener()