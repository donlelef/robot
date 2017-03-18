#! /usr/bin/env python3
"""
Test client for the <eduMorse> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

import sys
import time
import math

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

def print_position(position):

    print('({0:.3f}, {1:.3f})'.format(position['x'], position['y'], position['z']))

def print_dist_to_goal(distance):
     print('Distance to goal: {0:.3f}'.format(distance['near_robots']['GOAL']))
     
def get_min_range(robot):
    return min([robot.ir1.get()['range_list'][10], robot.ir2.get()['range_list'][10],robot.ir3.get()['range_list'][10]]) 

def get_yaw(robot):
    return robot.pose.get()['yaw']

def set_lin_vel(robot, vel):
    robot.motion.publish({'v': vel, 'w':0})

def set_ang_vel(robot, vel):
    robot.motion.publish({'v': 0, 'w': vel})

def go_straight(robot, vel):
    set_lin_vel(robot, vel)

def rotate_of(robot, degree, ang_vel):
    set_lin_vel(robot, 0)
    print('Stopped')
    target_yaw = get_yaw(robot) + degree
    set_ang_vel(robot, ang_vel)
    print('Rotating')
    delta = 0.05
    while ((get_yaw(robot) > target_yaw - delta) & (get_yaw(robot) < target_yaw + delta)) == False:
        pass
    set_ang_vel(robot, 0) 
    print('Stop rotating')  

def rotate_to(robot, degree, ang_vel):
    set_lin_vel(robot, 0)
    print('Stopped')
    target_yaw = degree
    set_ang_vel(robot, ang_vel)
    print('Rotating')
    delta = 0.05
    while ((get_yaw(robot) > target_yaw - delta) & (get_yaw(robot) < target_yaw + delta)) == False:
        pass
    set_ang_vel(robot, 0) 
    print('Stop rotating')

def robot_is_free(robot):
    range = get_min_range(robot)
    return range > 1.8

def rotate_to_freedom(robot, ang_vel):
    set_lin_vel(robot, 0)
    print('Stopped')
    set_ang_vel(robot, ang_vel)
    print('Rotating')
    while (robot_is_free(robot)) == False:
        pass
    set_ang_vel(robot, 0) 
    print('Stop rotating')

with Morse() as sim:

    rob = sim.robot
    v = 1.5
    w = 1
    degree = -(math.pi / 2)
    go_straight(rob, v)

    while True:
        if robot_is_free(rob) == False:
            print('Obtacle detected front')
            rotate_to_freedom(rob, w)
            go_straight(rob, v)
            print('Going straight')
       
