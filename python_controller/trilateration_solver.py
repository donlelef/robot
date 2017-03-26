import numpy as np
from Geometry2D import Point2D, Line2D

class TrilaterationSolver:

    tolerance = None

    def __init__(self, tolerance):
        """ Initializes the solver with a given tolerance """
        self.tolerance = tolerance

    def solve(self, x1, y1, r1, x2, y2, r2, x3, y3, r3):
        """ Trilaterate a target position given three points and their distance from it """
        if Line2D.are_collinear(Point2D(x1, y1), Point2D(x2, y2), Point2D(x3, y3), self.tolerance):
            raise Exception()

        P1 = np.array([x1, y1])
        P2 = np.array([x2, y2])
        P3 = np.array([x3, y3])

        ex = (P2 - P1) / np.linalg.norm((P2 - P1))
        i = np.dot(ex, (P3 - P1))
        ey = (P3 - P1 - i * ex) / np.linalg.norm((P3 - P1 - i * ex))
        d = np.linalg.norm((P2 - P1))
        j = np.dot(ey, (P3 - P1))
        x = (r1**2 - r2**2 + d**2) / (2 * d)
        y = (r1**2 - r3**2 + i**2 + j**2) / (2 * j) - (i * x) / j
        target = P1 + x*ex + y*ey

        return Point2D(target[0], target[1])
