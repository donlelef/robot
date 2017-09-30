from crash_generator.robot import Robot


class SimpleMotion(object):
    _linear_vel = None
    _angular_vel = None
    _exit_condition = None
    _robot = None

    def __init__(self, robot: Robot, linear_vel, angular_vel, exit_condition):
        self._robot = robot
        self._linear_vel = linear_vel
        self._angular_vel = angular_vel
        self._exit_condition = exit_condition

    def go_until_exit(self):
        while (not self._exit_condition.evaluate()) and (not self._risk_of_collision()):
            self._robot.set_velocity(self._linear_vel, self._angular_vel).stop_after(0.2)
        self._robot.stop()

    def _risk_of_collision(self):
        return min([self._robot.free_space_ahead, self._robot.free_space_left,
                    self._robot.free_space_right]) < self._robot.SENSORS_RANGE
