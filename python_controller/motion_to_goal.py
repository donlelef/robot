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
        robot.rotate_to(goal_orientation, self.rotation_velocity)

    def __init__(self, robot, goal, motion_velocity, rot_velocity):
        self.robot = robot
        self.goal = goal
        self.motion_velocity = motion_velocity
        self.rotation_velocity = rot_velocity

    def go_until_target_or_obstacle(self):
        print("Straaaaaight to the target, sir!")
        while self.robot.free_space_ahead >= robot.SENSOR_RANGE and self.robot.distance_to_target >= 2:
            time.sleep(0.5)
            robot.stop()
            self._rotate_to_goal()
            robot.set_velocity(self.motion_velocity, 0)
        robot.stop()




