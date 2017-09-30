import math
from threading import Timer


class MotionToGoal(object):
    TIME_OF_DRIFT = 2

    robot = None
    goal = None
    motion_velocity = None
    rotation_velocity = None
    _route_recompute = True

    def __init__(self, robot, goal, motion_velocity=2, rot_velocity=2):
        self.robot = robot
        self.goal = goal
        self.motion_velocity = motion_velocity
        self.rotation_velocity = rot_velocity

    def go_until_target_or_obstacle(self):
        self.robot.stop()
        print("Straaaaaight to the target, sir!")
        while self.robot.free_space_ahead >= self.robot.SENSORS_RANGE and self.robot.distance_to_target >= 2:
            if self._route_recompute:
                self.robot.stop()
                self._rotate_to_goal()
                self._route_recompute = False
                Timer(self.TIME_OF_DRIFT, self._set_recompute_flag).start()
                self.robot.set_velocity(self.motion_velocity, 0)

    def _rotate_to_goal(self):
        vector_to_goal = self.goal - self.robot.position
        goal_orientation = math.atan2(vector_to_goal.y, vector_to_goal.x)
        self.robot.rotate_to(goal_orientation, self.rotation_velocity)

    def _set_recompute_flag(self):
        self._route_recompute = True
