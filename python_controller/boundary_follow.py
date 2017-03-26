from robot import Robot

class Bug2BoundaryFollower(object):

    ANGULAR_VELOCITY = 2
    LINEAR_VELOCITY = 2
    MAX_FREE_SPACE = 1.5
    MIN_FREE_SPACE = 1
    LINE_TOLERANCE = 0.5
    INITIAL_POSITION_TOLERANCE = 1

    _robot = None
    _line_to_goal = None
    _hit_point = None

    def __init__(self, robot, goal):
        self._robot = robot
        self._hit_point = robot.position
        self._line_to_goal = Line2D.from_two_points(self._hit_point, goal)

    def follow_till_exit(self):
        """ Makes the robot follow the boundary of the obstacle until an exit condition is verified """
        while not self._exit_boundary_following():
            if robot.free_space_ahead < robot.SENSOR_RANGE:
                robot.set_velocity(0, -ANGULAR_VELOCITY)
                while robot.free_space_ahead < robot.SENSOR_RANGE:
                    pass
            elif robot.free_space_left < MIN_FREE_SPACE :
                robot.set_velocity(LINEAR_VELOCITY, -ANGULAR_VELOCITY)
                while robot.free_space_left < MIN_FREE_SPACE:
                    pass
            elif robot.free_space_left > MAX_FREE_SPACE:
                robot.set_velocity(LINEAR_VELOCITY, ANGULAR_VELOCITY)
                while robot.free_space_left > MAX_FREE_SPACE:
                    pass
            robot.set_velocity(LINEAR_VELOCITY, 0)

    def _exit_boundary_following(self):
        (not self._is_on_the_line()) or self._is_on_hit_point()

    def _is_on_the_line(self):
        return self._line_to_goal.contains_point(robot.position, LINE_TOLERANCE)

    def _is_on_hit_point(self):
        return self._hit_point.is_close_to(robot.position, INITIAL_POSITION_TOLERANCE)
