#!/usr/bin/env python

import rospy
import intera_interface

rospy.init_node("head",anonymous=True)

head = intera_interface.Head()
head.set_pan(-1.0)
