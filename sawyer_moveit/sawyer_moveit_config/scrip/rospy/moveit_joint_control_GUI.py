#!/usr/bin/env python
import sys
import copy
import rospy
#import intera_interface
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import time

from Tkinter import *
from math import pi
from std_msgs.msg import String
from std_msgs.msg import Float64
from moveit_commander.conversions import pose_to_list


sys.argv.append('joint_states:=/robot/joint_states')

moveit_commander.roscpp_initialize(sys.argv)
#Initial new node
rospy.init_node('move_group_python', anonymous=True)
#For turnable table

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "right_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
print"move_group",move_group
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
# We can get the name of the reference frame for this robot:
planning_frame = move_group.get_planning_frame()
print "============ Planning frame: %s" % planning_frame
print "============ Robot State "
print robot.get_current_state()
#group_names = robot.get_group_names()
print "============ Available Planning Groups:", robot.get_group_names()
#hand_pad = move_group.get_current_head_value()
#eef_link = move_group.get_end_effector_link()
#print "============ End effector link: %s" % eef_link
while not rospy.is_shutdown():
        try:
        	root = Tk()
        	root.title("MoveIt!")
        	def CallbackFunction_Turnable(speed):
        		position_turnable = t_data.get()
        		publisher.publish (position_turnable*pi/180)
        	#def CallbackFunction_head_pan(angle):
        	#	angle = s_data7.get()
        	#	head = intera_interface.Head()
        	#	head.set_pan(angle)
        	def CallbackFunction_Sawyer():
        		start_time= time.time()
        		joint_goal = move_group.get_current_joint_values()
        		print"joint", joint_goal
        		joint_goal[0] = s_data0.get()#*pi/180
        		joint_goal[1] = s_data1.get()#*pi/180
        		joint_goal[2] = s_data2.get()#*pi/180
        		joint_goal[3] = s_data3.get()#*pi/180
        		joint_goal[4] = s_data4.get()#*pi/180
        		joint_goal[5] = s_data5.get()#*pi/180
        		joint_goal[6] = s_data6.get()#*pi/180
        		#hand_pad = move_group.get_head_pen()
        		#joint_goal[7] = s_data7.get()
        		move_group.go(joint_goal, wait=True)
        	def CallbackFunction_Stop():
        		move_group.stop()

       	    	t_data = DoubleVar()
       	    	s_data0 = DoubleVar()
       	    	s_data1 = DoubleVar()
       	    	s_data2 = DoubleVar()
       	    	s_data3 = DoubleVar()
       	    	s_data4 = DoubleVar()
       	    	s_data5 = DoubleVar()
       	    	s_data6 = DoubleVar()
       	    	#s_data7 = DoubleVar()
       	    	data_time = StringVar()

       	    	
       	    	s0 = Scale(root, from_ = -3.0503, to = 3.0503, orient = HORIZONTAL, variable = s_data0, length =250, width = 10,digits= 4, resolution=0.01).grid(row=3, column = 1)
       	    	s1 = Scale(root, from_ = -3.8095, to = 2.2736, orient = HORIZONTAL, variable = s_data1, length =250, width = 10,digits= 4, resolution=0.0).grid(row=4, column = 1)
       	    	s2 = Scale(root, from_ = -3.0426, to = 3.0426, orient = HORIZONTAL, variable = s_data2, length =250, width = 10,digits= 4, resolution=0.0).grid(row=5, column = 1)
       	    	s3 = Scale(root, from_ = -3.0439, to = 3.0439, orient = HORIZONTAL, variable = s_data3, length =250, width = 10,digits= 4, resolution=0.0).grid(row=6, column = 1)
       	    	s4 = Scale(root, from_ = -2.9761, to = 2.9761, orient = HORIZONTAL, variable = s_data4, length =250, width = 10,digits= 4, resolution=0.0).grid(row=7, column = 1)
       	    	s5 = Scale(root, from_ = -2.9761, to = 2.9761, orient = HORIZONTAL, variable = s_data5, length =250, width = 10,digits= 4, resolution=0.0).grid(row=8, column = 1)
       	    	s6 = Scale(root, from_ = -3.14, to = 3.14, orient = HORIZONTAL, variable = s_data6, length =250, width = 10,digits= 4, resolution=0.0).grid(row=9, column = 1)
       	    	#s7 = Scale(root, from_ = -5.0952, to = 0.9064, orient = HORIZONTAL, variable = s_data7, command = CallbackFunction_head_pan,length =250, width = 10,digits= 4, resolution=0.0).grid(row=10, column = 1)

       	    	
       	    	Label(root, text='Sawyer_Joint').grid(row=2,column=0)
       	    	Label(root, text='Joint_0').grid(row=3,column=0)
       	    	Label(root, text='Joint_1').grid(row=4,column=0)
       	    	Label(root, text='Joint_2').grid(row=5,column=0)
       	    	Label(root, text='Joint_3').grid(row=6,column=0)
       	    	Label(root, text='Joint_4').grid(row=7,column=0)
       	    	Label(root, text='Joint_5').grid(row=8,column=0)
       	    	Label(root, text='Joint_6').grid(row=9,column=0)
       	    	#Label(root, text='Joint_7').grid(row=10,column=0)
       	    	#Label(root,textvariable = data_time).grid(row=7, column =1)
       	    	#Label(root,textvariable= data_position).grid(row= 8, column = 1)

       	    	Button(text="Go to joint", command = CallbackFunction_Sawyer).grid(row = 12, column=0)
	    	Button(text="Stop", command = CallbackFunction_Stop).grid(row = 12, column=1)
	   	root.mainloop()
        except KeyboardInterrupt:
            print "Ctrl+c"
            break


#joint_goal = move_group.get_current_joint_values()
#joint_goal[0] = 0
#joint_goal[1] = -pi/4
#joint_goal[2] = 0
#joint_goal[3] = -pi/2
#joint_goal[4] = 0
#joint_goal[5] = pi/3
#joint_goal[6] = 0
#move_group.go(joint_goal, wait=True)
#move_group.stop()
#pose_goal = geometry_msgs.msg.Pose()
#pose_goal.orientation.w = 1.0
#pose_goal.position.x = 0.5
#pose_goal.position.y = 0.5
#pose_goal.position.z = 0.5
#move_group.set_pose_target(pose_goal)
#plan = move_group.go(wait=True)
# We can also print the name of the end-effector link for this group:
#eef_link = move_group.get_end_effector_link()
#print "============ End effector link: %s" % eef_link

# We can get a list of all the groups in the robot:
#group_names = robot.get_group_names()
#    print "============ Available Planning Groups:", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
#print "============ Printing robot state"
#print robot.get_current_state()
#print ""## END_SUB_TUTORIAL
