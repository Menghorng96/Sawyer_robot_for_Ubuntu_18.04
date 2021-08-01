#! /usr/bin/env python

import rospy
import intera_interface
import time
import math
c= 0.0
rospy.init_node('velocity')

limb_mv = intera_interface.Limb('right')
#set velocity of each joint angle
#limb_mv.set_joint_velocities(5.0)
limb_mv.move_to_neutral()
#limb_mv.set_joint_velocities(0.01)
#Joint angle position
home_pose = {'right_j6': 0.0 ,'right_j5': 0.0 ,'right_j4': 0.0 ,'right_j3': 0.0 ,'right_j2': 0.0 ,'right_j1': 0.0 + c ,'right_j0': -0.0}
#Set velovcity on joint angle 5
limb_mv.set_joint_velocities('right_j5',0.3)
#Set the position of the robot
limb_mv.set_joint_positions(home_pose)

#limb_mv.move_to_joint_positions(home_pose)
#limb_mv.set_joint_velocities(0.01)
#limb_mv.joint_velocities()
