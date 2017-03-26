#! /usr/bin/env python3

from robot import Robot

try:
    from pymorse import Morse
except ImportError:
    print("You need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)


with Morse() as sim:
    robot = Robot(sim.robot)
    robot.stop()

