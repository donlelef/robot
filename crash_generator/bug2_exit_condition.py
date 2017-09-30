from crash_generator.trilateration.planar_geometry import Line2D


class Bug2ExitCondition(object):

    LINE_TOLERANCE = 0.5
    INITIAL_POSITION_TOLERANCE = 5

    _robot = None
    _line_to_goal = None
    _hit_point = None

    def __init__(self, robot, goal):
        self._robot = robot
        self._hit_point = robot.position
        self._line_to_goal = Line2D.from_two_points(self._hit_point, goal)

    def evaluate(self):
        return not self._keep_following()

    def _keep_following(self):
        return (not self._is_on_the_line()) or self._is_on_hit_point()

    def _is_on_the_line(self):
        return self._line_to_goal.contains_point(self._robot.position, self.LINE_TOLERANCE)

    def _is_on_hit_point(self):
        return self._hit_point.is_close_to(self._robot.position, self.INITIAL_POSITION_TOLERANCE)
