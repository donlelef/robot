#! /usr/bin/env python3
import sys
from robot import Robot
from trilateration_solver import TrilaterationSolver
from robot_trilaterator import RobotTrilaterator
from trilaterator import Trilaterator
from simple_motion import SimpleMotion
from boundary_follow import BoundaryFollower
from bug2_exit_condition import Bug2ExitCondition
from motion_to_goal import MotionToGoal
from pymorse import Morse

with Morse() as sim:

    robot = Robot(sim.robot)

    '''start tmp'''
    tril_solver = TrilaterationSolver(0.25)
    trilaterator = Trilaterator(robot, tril_solver)
    motion = SimpleMotion(robot, 0.1, 0.1, trilaterator)
    boundary = BoundaryFollower(robot, trilaterator)

    motion.go_until_exit()
    print('mmmm')
    if trilaterator.goal == None:
        print('allahu akbar')
        boundary.follow_till_exit()
    robot.stop()
    goal = trilaterator.goal
    print('Target acquired at {}... going for conquer, sir!'.format(goal))
    '''end tmp'''

    motion = MotionToGoal(robot, goal)
    boundary = BoundaryFollower(robot, Bug2ExitCondition(robot, goal))

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

