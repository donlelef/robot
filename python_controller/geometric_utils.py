#! /usr/bin/env python3

import math

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


'''
A class representing a 2d straight line using the formula ax + by + c = 0
'''
class Line2D:
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.a, self.b, self.c)

    def contains_point(self, point, tolerance):
        return a * point.x + b * point.y + c < tolerance

    @staticmethod
    def from_two_points(point_1, point_2):
        if(not Line2D._are_parallel_to_y(point_1, point_2)):
            m = (point_2.y - point_1.y) / (point_2.x - point_1.x)
            q = (-1 * m * point_1.x) + point_1.y
            return Line2D.from_explicit_form(m, q)    
        else:
            return Line2D(1, 0, - point_1.x)

    @staticmethod 
    def from_explicit_form(m, q):
        return Line2D(-m, 1, -q)

    @staticmethod
    def are_collinear(self, p1, p2, p3, tolerance):
        return abs((p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)) < self.tolerance

    @staticmethod
    def _are_parallel_to_y(point1, point2):
        return point1.x == point2.x


def main(): 
line1 = Line2D.from_two_points(Position2D(0, 0), Position2D(1, 1))
print(str(line1))
line2 = Line2D.from_two_points(Position2D(2, 3), Position2D(2, 6))
print(str(line2))

if __name__ == "__main__":
    main()


