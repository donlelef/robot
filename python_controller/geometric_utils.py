#! /usr/bin/env python3

import math

class GeometricUtils:

    tolerance = None

    def __init__(self, tolerance):
        self.tolerance = tolerance

    def check_if_collinear(self, p1, p2, p3):
        return abs((p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)) < self.tolerance

class Position2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)

    def __add__(self, other):
        return Position2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position2D(self.x - other.x, self.y - other.y)

    @staticmethod
    def from_morse(morse_position):
        x = morse_position['x']
        y = morse_position['y']
        return Position2D(x, y)


class Line2D:

    m = None
    q = None

    def __init__(self, m, q):
        self.m = m
        self.q = q

    def __str__(self):
        return "y = {}x + {}".format(self.m, self.q)

    def contains_point(self, point, tolerance):
        return point.y - self.m * point.x - self.q < tolerance

    @staticmethod
    def from_two_points(point_1, point_2):
        '''TODO Lele, you are the Math geek'''
        m = (point_2.y  - point_1.y) / (point_2.x - point_1.x)
        q = (-1 * m * point_1.x) + point_1.y
        return Line2D(m, q)
