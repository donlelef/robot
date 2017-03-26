from robot import Robot
from Line2D import Line2D


class Bug2BoundaryFollower(object):

    ANGULAR_VELOCITY = 2
    LINEAR_VELOCITY = 2
    MAX_FREE_SPACE = 1.5
    MIN_FREE_SPACE = 1
    LINE_TOLERANCE = 0.5
    INITIAL_POSITION_TOLERANCE = 5

    _robot = None
    _line_to_goal = None
    _hit_point = None

    def __init__(self, robot, goal):
        self._robot = robot
        self._hit_point = robot.position
        self._line_to_goal = Line2D.from_two_points(self._hit_point, goal)

    def follow_till_exit(self):
        """ Makes the robot follow the boundary of the obstacle until an exit condition is verified """
        while self._keep_following():
            if self._robot.free_space_ahead < self._robot.SENSORS_RANGE:
                self._robot.set_velocity(0, -self.ANGULAR_VELOCITY)
                while self._robot.free_space_ahead < self._robot.SENSORS_RANGE:
                    pass
            elif self._robot.free_space_left < self.MIN_FREE_SPACE:
                self._robot.set_velocity(
                    self.LINEAR_VELOCITY, -self.ANGULAR_VELOCITY)
                while self._robot.free_space_left < self.MIN_FREE_SPACE:
                    pass
            elif self._robot.free_space_left > self.MAX_FREE_SPACE:
                self._robot.set_velocity(
                    self.LINEAR_VELOCITY, self.ANGULAR_VELOCITY)
                while self._robot.free_space_left > self.MAX_FREE_SPACE:
                    pass
            self._robot.set_velocity(self.LINEAR_VELOCITY, 0)

    def _keep_following(self):
        return (not self._is_on_the_line()) or self._is_on_hit_point()

    def _is_on_the_line(self):
        return self._line_to_goal.contains_point(self._robot.position, self.LINE_TOLERANCE)

    def _is_on_hit_point(self):
        return self._hit_point.is_close_to(self._robot.position, self.INITIAL_POSITION_TOLERANCE)
