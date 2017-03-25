#! /usr/bin/env python3
import sys
import time
import math
import numpy as np
from robot import Robot
from trilateration_solver import TrilaterationSolver
from boundary_follow import Bug2BoundaryFollower
from motion_to_goal import MotionToGoal
from Geometry2D import Point2D, Line2D

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

    motion = MotionToGoal(robot, goal)
    exit_condition = lambda robot, line_to_goal: (not line_to_goal.contains_point(robot.position, 0.5)) or initial_position.is_close_to(robot.position, 1)
    boundary = Bug2BoundaryFollower(robot, exit_condition)

    while True:

        motion.go_until_target_or_obstacle()

        if robot.distance_to_target < 2:
            print("On the target, sir!")
            break

        if robot.free_space_ahead < robot.SENSORS_RANGE:
            print("Entering boundary following")
            boundary.follow_till_exit()
            print("Exiting boundary following")
