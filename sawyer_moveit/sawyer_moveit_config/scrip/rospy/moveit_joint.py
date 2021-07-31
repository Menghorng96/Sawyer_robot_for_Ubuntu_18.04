#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from Tkinter import *
from PIL  import ImageTk, Image
import numpy as np
import math
import time
import numpy as np
from rdp import rdp
from tf.transformations import quaternion_from_euler
from math import pi
from std_msgs.msg import String
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from moveit_commander.conversions import pose_to_list

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager



if __name__=="__main__":
    sys.argv.append('joint_states:=/robot/joint_states')

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python', anonymous=True)
    #Turnable
    turnable = rospy.Publisher('/robot/right_joint_position_controller/joints/Turnable_Table_joint_controller/command',Float64, queue_size=1.0)
    #sawyer
    robot = moveit_commander.RobotCommander()
    #scene = moveit_commander.PlanningSceneInterface()
    group_name = "right_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    #display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    #display_trajectory.trajectory_start = robot.get_current_state()
    #display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

    #planning_frame = move_group.get_planning_frame()
    #pose_goal = geometry_msgs.msg.Pose()
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0]= 0.0
    joint_goal[1] = -1.0
    joint_goal[2]= 0.0
    joint_goal[3]= 2.0
    joint_goal[4]= 0.0
    joint_goal[5]= 0.567
    joint_goal[6]= -1.4

    plan=move_group.go(joint_goal, wait= True)
    print"plan",plan
    while plan == False:
        plan = move_group.go(joint_goal, wait= True)
