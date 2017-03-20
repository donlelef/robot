import numpy as np
from position import Position2D

class TrilaterationSolver:
    
    @staticmethod
    def trilaterate(x1, y1, r1, x2, y2, r2, x3, y3, r3):
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