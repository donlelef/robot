from crash_generator import configuration
from crash_generator.robot.robot import Robot


class ConstantMotion(object):
    def __init__(self, robot: Robot, linear_vel, angular_vel, exit_condition):
        self._robot = robot
        self._linear_vel = linear_vel
        self._angular_vel = angular_vel
        self._exit_condition = exit_condition

    def go_until_exit(self):
        while not (self._exit_condition.evaluate() or self._risk_of_collision()):
            self._robot.set_velocity(self._linear_vel, self._angular_vel)
            self._robot.sleep(configuration.SAMPLE_TIME)
        self._robot.stop()

    def _risk_of_collision(self):
        print([self._robot.free_space_ahead, self._robot.free_space_left, self._robot.free_space_right])
        return min([self._robot.free_space_ahead, self._robot.free_space_left,
                    self._robot.free_space_right]) < self._robot.SENSORS_RANGE