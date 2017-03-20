#! /usr/bin/env python3

from position import Position2D
import math

class GeometricUtils:

    tolerance = None

    def __init__(self, tolerance):
        self.tolerance = tolerance

    def check_if_collinear(self, p1, p2, p3):
        return abs((p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)) < self.tolerance
