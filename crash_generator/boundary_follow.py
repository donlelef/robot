from crash_generator.robot import Robot


class BoundaryFollower(object):
    """Generic algorithm for boundary following with boolean exit condition"""

    ANGULAR_VELOCITY = 2
    LINEAR_VELOCITY = 2
    MAX_FREE_SPACE = 1.5
    MIN_FREE_SPACE = 1

    _exit_condition = None
    _robot = None

    def __init__(self, robot: Robot, exit_condition):
        self._robot = robot
        self._exit_condition = exit_condition

    def follow_till_exit(self):
        """ Makes the robot follow the boundary of the obstacle while a certain condition is met """
        while not self._exit_condition.evaluate():
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
            self._robot.set_velocity(self.LINEAR_VELOCITY, 0).sleep(0.1)


