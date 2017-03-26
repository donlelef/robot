#! /usr/bin/env python3
import sys
from robot import Robot
from trilateration_solver import TrilaterationSolver
from robot_trilaterator import RobotTrilaterator
from boundary_follow import Bug2BoundaryFollower
from motion_to_goal import MotionToGoal

try:
    from pymorse import Morse
except ImportError:
    print("You need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

with Morse() as sim:

    robot = Robot(sim.robot)
    robot.stop()

    goal = RobotTrilaterator(robot, TrilaterationSolver(0.01)).trilaterate_goal()    

    motion = MotionToGoal(robot, goal)
    boundary = Bug2BoundaryFollower(robot, goal)

    while True:

        motion.go_until_target_or_obstacle()

        if robot.distance_to_target < 2.5:
            print("On the target, sir!")
            break

        if robot.free_space_ahead < robot.SENSORS_RANGE:
            print("Following the bondary until victory, sir!")
            boundary.follow_till_exit()
            print("Leaving this boundary, sir!")

    robot.stop()

