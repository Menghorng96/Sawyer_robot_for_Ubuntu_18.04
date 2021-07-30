#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
import time
from tf.transformations import quaternion_from_euler
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

sys.argv.append('joint_states:=/robot/joint_states')

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python', anonymous=True)


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

start_time = time.time()
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "right_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
# We can get the name of the reference frame for this robot:
#planning_frame = move_group.get_planning_frame()
#print "============ Planning frame: %s" % planning_frame
#print "============ Robot State "
#print robot.get_current_state()
#eef_link = move_group.get_end_effector_link()
#print "============ End effector link: %s" % eef_link
#rospy.sleep(2)
#box_pose = geometry_msgs.msg.PoseStamped()
#box_pose.header.frame_id = "rotation_Link"
#box_pose.pose.position.z = 0.238# slightly above the end effector
#box_name = "box"
#scene.add_box(box_name, box_pose,(0.4, 0.4, 0.4))
#scene.attach_box("rotation_Link", box_name)

#pose_goal = geometry_msgs.msg.Pose()
#pose_goal.orientation.w = 0.5
#pose_goal.position.x = 0.8
#pose_goal.position.y = 0.0
#pose_goal.position.z = 0.638

#roll_angle=0.0
#pitch_angle= 0.0
#yaw_angle=0.0

#quaternion = quaternion_from_euler(roll_angle, pitch_angle, yaw_angle)
#pose_goal.orientation.x =quaternion[0]
#pose_goal.orientation.y = quaternion[1]
#pose_goal.orientation.z = quaternion[2]
#pose_goal.orientation.w = quaternion[3]
#move_group.set_pose_target(pose_goal)
#print(move_group.get_planning_time())#seconds
#move_group.plan(pose_goal)
#plan = move_group.go(wait=True)
#print(plan)
#if plan== False:
#	print("Menghorng1")
def display_trajectory(plan):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.
    #robot = self.robot
    #display_trajectory_publisher = self.display_trajectory_publisher

    ## BEGIN_SUB_TUTORIAL display_trajectory
    ##
    ## Displaying a Trajectory
    ## ^^^^^^^^^^^^^^^^^^^^^^^
    ## You can ask RViz to visualize a plan (aka trajectory) for you. But the
    ## group.plan() method does this automatically so this is not that useful
    ## here (it just displays the same trajectory again):
    ##
    ## A `DisplayTrajectory`_ msg has two primary fields, trajectory_start and trajectory.
    ## We populate the trajectory_start with our current robot state to copy over
    ## any AttachedCollisionObjects and add our plan to the trajectory.
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    # Publish
    display_trajectory_publisher.publish(display_trajectory);

    ## END_SUB_TUTORIAL
def plan_cartesian_path( scale=1):
    waypoints = []

    wpose = move_group.get_current_pose().pose
    wpose.position.z -= scale * 0.1  # First move up (z)
    wpose.position.y += scale * 0.2  # and sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y -= scale * 0.1  # Third move sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.
    print (waypoints)
    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction


cartesian_plan, fraction = plan_cartesian_path(scale=1)
print("Hello")
print (cartesian_plan)
#display_trajectory(cartesian_plan)
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
#print ""
## END_SUB_TUTORIAL

