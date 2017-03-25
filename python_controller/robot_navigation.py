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
from trilateration_solver import TrilaterationSolver
from geometric_utils import *
import math


def ahead_not_free(robot):
    return robot.ahead_range < 2


def left_too_far(robot):
    return robot.at_left_range > 1.5


def left_too_near(robot):
    return robot.at_left_range < 1


def rotate_to_goal(robot, goal, velocity):
    vector_to_goal = goal - robot.position
    goal_orientation = math.atan2(vector_to_goal.y, vector_to_goal.x)
    required_rotation_angle = goal_orientation - robot.orientation
    robot.rotate_of(required_rotation_angle, velocity)


try:
    from pymorse import Morse
except ImportError:
    print("You need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

with Morse() as sim:

    robot = Robot(sim.robot)
    robot.stop()
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

    line_to_goal = Line2D.from_two_points(robot.position, goal)
    rotate_to_goal(robot, goal, 1)
    robot.set_velocity(2, 0)

    while True:

        '''TODO: capire se e come togliere lo sleep'''
        while robot.ahead_range >= 2 and robot.distance_to_target >= 2:
            '''motion to goal phase'''
            time.sleep(0.5)
            robot.stop()
            rotate_to_goal(robot, goal, 1)
            robot.set_velocity(2, 0)

        if robot.distance_to_target < 2:
            '''target reached'''
            print("On the target, sir!")
            break

        if robot.ahead_range < 2:
            '''wall reached -> boundary following phase'''
            print("Entering boundary following")
            initial_distance = robot.distance_to_target
            initial_position = robot.position
            while (not line_to_goal.contains_point(robot.position, 0.5)) or initial_position.is_close_to(robot.position, 1):
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
            print("Exiting boundary following")
