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
from robot import Robot
from position import Position2D
from trilateration_solver import TrilaterationSolver

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

with Morse() as sim:

    robot = Robot(sim.robot)

    pos1 = robot.position
    r1 = robot.distance_to_target

    robot.set_velocity(1, 0).stop_after(1)

    pos2 = robot.position
    r2 = robot.distance_to_target
    
    robot.set_velocity(1, 0).stop_after(1)

    pos3 = robot.position
    r3 = robot.distance_to_target

    goal = TrilaterationSolver.trilaterate_using_projections(pos1.x, pos1.y, r1, pos2.x, pos2.y, r2, pos3.x, pos3.y, r3)

    print(str(goal))
