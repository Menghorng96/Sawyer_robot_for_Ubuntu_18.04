#! /usr/bin/env python

import rospy
import intera_interface

#Intial Node
rospy.init_node('joint_angle')
#Intial intera interface
limb_mv = intera_interface.Limb('right')
# set joint angle to each joint of robot arm
home_pose = {'right_j6': 3.3161 ,'right_j5': 0.57 ,'right_j4': 0.0 ,'right_j3': 2.18 ,'right_j2': 0.0 ,'right_j1': -1.18 ,'right_j0': 0.0}
# Move joint angle that has set
limb_mv.move_to_joint_positions(home_pose) ###robot go to natural position
print (limb_mv.endpoint_pose())#Print end-effector position
