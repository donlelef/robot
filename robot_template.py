#! /usr/bin/env python3
"""
Test client for the <eduMorse> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

import sys
import time

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

def print_position(position):

    print('({0:.3f}, {1:.3f})'.format(position['x'], position['y'], position['z']))

def print_dist_to_goal(distance):
     print('Distance to goal: {0:.3f}'.format(distance['near_robots']['GOAL']))
     
def get_ranges(robot):
    return [robot.ir1.get()['range_list'][10], robot.ir4.get()['range_list'][10]]

with Morse() as sim:

    rob = sim.robot
    vel = 1
    rob.motion.publish({'v': vel, 'w':0})

    while True:
        if min(get_ranges(rob)) < 1.5:
            vel = -vel
            rob.motion.publish({'v': vel, 'w':0})
            print('Inverting motion direction')

       
