import sys

from crash_generator.robot.robot import Robot

try:
    from pymorse import Morse
except ImportError:
    print("You need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)


with Morse() as sim:
    robot = Robot(sim.robot, sim)
    robot.stop()

