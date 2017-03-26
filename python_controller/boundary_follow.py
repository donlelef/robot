from robot import Robot

class Bug2BoundaryFollower(object):

    robot = None

    def __init__(self, robot, exit_condition):
        self.robot = robot
        self.exit_condition = exit_condition

    def follow_till_exit(self):
        """ Makes the robot follow the boundary of the obstacle until an exit condition is verified """
        while not self.exit_condition(robot, line_to_goal):
            if robot.free_space_ahead < robot.SENSOR_RANGE:
                robot.set_velocity(0, -2)
                while robot.free_space_ahead < robot.SENSOR_RANGE:
                    pass
            elif robot.free_space_left < 1 :
                robot.set_velocity(2, -2)
                while robot.free_space_left < 1:
                    pass
            elif robot.free_space_left > 1.5:
                robot.set_velocity(2, 2)
                while robot.free_space_left > 1.5:
                    pass
            robot.set_velocity(2, 0)


