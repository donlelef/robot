from trilateration_solver import TrilaterationSolver
from Line2D import Line2D

class Trilaterator(object):

    _distances_by_position = {}
    _robot = None
    goal = None

    def __init__(self, robot, solver):
        self._robot = robot
        self._solver = solver

    def _add_record(self):
        keys = [k for k in self._distances_by_position]
        self._robot.stop()
        new_p = self._robot.position
        new_d = self._robot.distance_to_target
        if len(keys) == 0:
            self._distances_by_position[new_p] = new_d
        elif len(keys) == 1:
            if not keys[0].is_close_to(new_p, 0.5):
                self._distances_by_position[new_p] = new_d
        else:
            p1 = keys[0]
            p2 = keys[1]
            if not Line2D.are_collinear(p1, p2, new_p, 0.5):
                self._distances_by_position[new_p] = new_d

    def evaluate(self):
        self._add_record()
        keys = [k for k in self._distances_by_position]
        values = [self._distances_by_position[k] for k in keys]
        if len(self._distances_by_position) == 3:
            p1 = keys[0]
            r1 = values[0]
            p2 = keys[1]
            r2 = values[1]
            p3 = keys[2]
            r3 = values[2]
            self.goal = self._solver.solve(p1.x, p1.y, r1, p2.x, p2.y, r2, p3.x, p3.y, r3)
            return True
        return False


