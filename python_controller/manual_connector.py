#! /usr/bin/env python3

from robot import Robot
from pymorse import Morse

def robot():
    return Robot(Morse().robot)