#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 23:01:43 2022

@author: ozgur
"""
"""Driver for locosys GPS for moborobo"""

#import numpy as np
#import os, pynmea2, roslib, serial
import rospy
from nmea_msgs.msg import Sentence

file_name = 'gps_data.txt'

def callback(ros_data):
    '''Callback function of subscribed topic. '''
    header_time = str(ros_data.header.stamp.to_time())
    sentence = ros_data.sentence
    #header_time = str(rospy.Time.now().to_time())
    with open(file_name, "a") as myfile:
        myfile.write("New GPS Data:\n")
        myfile.write(header_time)
        myfile.write("\n")
        myfile.write(sentence)
        myfile.write("\n")
    
def main(robotname="moborobo"):
    gps_sub = rospy.Subscriber("%s/mygps"%robotname, Sentence, callback)
    rospy.spin()
    
if __name__ == "__main__":
    rospy.init_node('gps_Sub', anonymous=True)
    main()
