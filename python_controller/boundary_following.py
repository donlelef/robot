#! /usr/bin/env python3

import sys
import math
from robot import Robot
from position import Position2D

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

