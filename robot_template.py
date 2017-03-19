#! /usr/bin/env python3
"""
Test client for the <eduMorse> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

import sys
import numpy as np
import time

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

def set_vel(robot, linear_vel, angular_vel):
    robot.motion.publish({'v': linear_vel, 'w':angular_vel})

def get_xy_position(robot):
    position = robot.pose.get()
    return {'x': position['x'], 'y': position['y']}

def get_distance(robot):
    return robot.prox.get()['near_robots']['GOAL']

def stop(robot):
    set_vel(robot, 0, 0)

with Morse() as sim:

    rob = sim.robot

    pos1 = get_xy_position(rob)
    r1 = get_distance(rob)

    set_vel(rob, 1, 0.3)
    time.sleep(1)
    stop(rob)
    pos2 = get_xy_position(rob)
    r2 = get_distance(rob)
    
    set_vel(rob, 1, 0.3)
    time.sleep(1)
    stop(rob)
    pos3 = get_xy_position(rob)
    r3 = get_distance(rob)

    x1 = pos1['x']
    x2 = pos2['x']
    x3 = pos3['x']
    y1 = pos1['y']
    y2 = pos2['y']
    y3 = pos3['y']

    a = -2 * x1 + 2 * x2
    b = -2 * y1 + 2 * y2
    c = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    d = -2 * x2 + 2 * x3
    e = -2 * y2 + 2 * y3
    f = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

    A = np.array([[a, b], [d, e]])
    B = np.array([[c], [f]])

    goal = np.linalg.solve(A, B)

    print(str(goal))
