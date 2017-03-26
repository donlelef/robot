import math
import time

class MotionToGoal(object):

    robot = None
    goal = None
    motion_velocity = None
    rotation_velocity = None

    def _rotate_to_goal(self):
        vector_to_goal = self.goal - self.robot.position
        goal_orientation = math.atan2(vector_to_goal.y, vector_to_goal.x)
        self.robot.rotate_to(goal_orientation, self.rotation_velocity)

    def __init__(self, robot, goal, motion_velocity = 2, rot_velocity = 2):
        self.robot = robot
        self.goal = goal
        self.motion_velocity = motion_velocity
        self.rotation_velocity = rot_velocity

    def go_until_target_or_obstacle(self):
        self.robot.stop()
        print("Straaaaaight to the target, sir!")
        while self.robot.free_space_ahead >= self.robot.SENSORS_RANGE and self.robot.distance_to_target >= 2:
            self._rotate_to_goal()
            self.robot.set_velocity(self.motion_velocity, 0)
            time.sleep(0.5)
            self.robot.stop()

