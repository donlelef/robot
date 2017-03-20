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
from geometric_utils import GeometricUtils
import math


def ahead_not_free(robot):
    return robot.ahead_range < 2


def left_too_far(robot):
    return robot.at_left_range > 1.5


def left_too_near(robot):
    return robot.at_left_range < 1

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)


with Morse() as sim:

    robot = Robot(sim.robot)
    solver = TrilaterationSolver(0.01)

    pos1 = robot.position
    r1 = robot.distance_to_target

    robot.set_velocity(1, 1).stop_after(0.5)

    pos2 = robot.position
    r2 = robot.distance_to_target

    robot.set_velocity(1, 1).stop_after(0.5)

    pos3 = robot.position
    r3 = robot.distance_to_target

    goal = solver.trilaterate_using_projections(
        pos1.x, pos1.y, r1, pos2.x, pos2.y, r2, pos3.x, pos3.y, r3)

    state = 'motion_to_goal'

    while robot.distance_to_target > 3:
        if state == 'motion_to_goal':
            actual_position = pos3
            actual_orientation = robot.orientation
            vector_to_goal = goal - actual_position
            goal_orientation = math.atan2(vector_to_goal.y, vector_to_goal.x)
            required_rotation_angle = goal_orientation - actual_orientation

            robot.rotate_of(required_rotation_angle, 1)
            robot.set_velocity(100, 0)

            while (robot.ahead_range >= 2) & (robot.distance_to_target > 3):
                pass

            robot.stop()
            state = 'boudary_following'
            break

        if state == 'boudary_following':
            while True:
                if ahead_not_free(robot):
                    robot.set_velocity(0, -2)
                    while ahead_not_free(robot):
                        pass
                elif left_too_near(robot):
                    robot.set_velocity(2, -2)
                    while left_too_near(robot):
                        pass
                elif left_too_far(robot):
                    robot.set_velocity(2, 2)
                    while left_too_far(robot):
                        pass
            robot.set_velocity(2, 0)
    
    robot.stop()
