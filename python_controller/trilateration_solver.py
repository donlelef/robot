import numpy as np
from position import Position2D
from geometric_utils import GeometricUtils

class TrilaterationSolver:

    geometric_utils = None

    def __init__(self, tolerance):
        self.geometric_utils = GeometricUtils(tolerance)

    @staticmethod
    def _trilaterate(x1, y1, r1, x2, y2, r2, x3, y3, r3):
        a = -2 * x1 + 2 * x2
        b = -2 * y1 + 2 * y2
        c = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
        d = -2 * x2 + 2 * x3
        e = -2 * y2 + 2 * y3
        f = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

        A = np.array([[a, b], [d, e]])
        B = np.array([[c], [f]])

        object_position = np.linalg.solve(A, B)

        return Position2D(object_position[0][0], object_position[1][0])

    @staticmethod
    def trilaterate(pos1, r1, pos2, r2, pos3, r3):
        return TrilaterationSolver._trilaterate(pos1.x, pos1.y, r1, pos2.x, pos2.y, r2, pos3.x, pos3.y, r3)


    def trilaterate_using_projections(self, x1, y1, r1, x2, y2, r2, x3, y3, r3):
        if self.geometric_utils.check_if_collinear(Position2D(x1, y1), Position2D(x2, y2), Position2D(x3, y3)):
            print("Points are collinear")

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

        return Position2D(target[0], target[1])
