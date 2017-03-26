from trilateration_solver import TrilaterationSolver

class Trilaterator(object):

    _distances_by_position = {}
    _robot = None
    goal = None

    def __init__(self, robot, solver):
        self._robot = robot
        self._solver = solver

    def _add_record(self):
        new_p = self._robot.position
        new_d = self._robot.distance_to_target
        if len(self._distances_by_position) == 0:
            self._distances_by_position[new_p] = new_d
        elif len(self._distances_by_position) == 1:
            if not self._distances_by_position.keys[0].is_close_to(new_p, 0.25):
                self._distances_by_position[new_p] = new_d
        else:
            p1 = self._distances_by_position.keys[0]
            p2 = self._distances_by_position.keys[1]
            if not Line2D.are_collinear(p1, p2, new_p, 0.1):
                self._distances_by_position[new_p] = new_d

    def evaluate(self):
        self._add_record()
        if len(self._self._distances_by_position.keys) == 3:
            p1 = self._distances_by_position.keys[0]
            r1 = self._distances_by_position.values[0]
            p2 = self._distances_by_position.keys[1]
            r2 = self._distances_by_position.values[1]
            p3 = self._distances_by_position.keys[2]
            r3 = self._distances_by_position.values[2]
            goal = self._solver.solve(p1.x, p1.y, r1, p2.x, p2.y, r2, p3.x, p3.y, r3)
            return True
        return False


