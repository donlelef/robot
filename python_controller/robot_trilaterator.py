from robot import Robot

class RobotTrilaterator(object):
    """Execute a trilateration algorithm to get the position of the goal for a obot"""
    
    _robot = None
    _trilateration_algorithm = None

    def __init__(self, robot, trilateration_algorithm):
        self._robot = robot
        self._trilateration_algorithm = trilateration_algorithm

    def trilaterate_goal(self):
        """
        Get the position of the goal by trilaterating 3 distances.
        Distances are measured in 3 dinstinct points.
        """

        pos1 = self._robot.position
        r1 = self._robot.distance_to_target
        self._to_next_point()

        pos2 = self._robot.position
        r2 = self._robot.distance_to_target
        self._to_next_point()

        pos3 = self._robot.position
        r3 = self._robot.distance_to_target

        goal = self._trilateration_algorithm.solve(
            pos1.x, pos1.y, r1, pos2.x, pos2.y, r2, pos3.x, pos3.y, r3)

        return goal

    def _to_next_point(self):
        return self._robot.set_velocity(1, 1).stop_after(0.5)


