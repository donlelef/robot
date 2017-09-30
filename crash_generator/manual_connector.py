from crash_generator.robot import Robot
from pymorse import Morse


def robot():
    return Robot(Morse().robot)
