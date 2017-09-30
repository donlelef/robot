from pymorse import Morse

from crash_generator.motion_control.boundary_follow import BoundaryFollower
from crash_generator.motion_control.bug2_exit_condition import Bug2ExitCondition
from crash_generator.motion_control.motion_to_goal import MotionToGoal
from crash_generator.motion_control.simple_motion import ConstantMotion
from crash_generator.robot.robot import Robot
from crash_generator.trilateration.trilateration import Trilaterator
from crash_generator.trilateration.trilateration_solution import TrilaterationSolver

with Morse() as sim:
    robot = Robot(sim.robot, sim)

    '''start tmp'''
    trilaterator = Trilaterator(robot, TrilaterationSolver())
    motion = ConstantMotion(robot, 1, 1, trilaterator)
    boundary = BoundaryFollower(robot, trilaterator)

    motion.go_until_exit()
    print('Trilaterating or crashing, sir!')

    if trilaterator.goal is None:
        print('Wall detected. Following the boundary while trilaterating, sir!')
        boundary.follow_till_exit()

    robot.stop()
    goal = trilaterator.goal
    print('Target acquired at {}... going for conquer, sir!'.format(goal))
    '''end tmp'''

    motion = MotionToGoal(robot, goal)
    boundary = BoundaryFollower(robot, Bug2ExitCondition(robot, goal))

    while True:

        motion.go_until_target_or_obstacle()

        if robot.distance_to_target <= robot.SENSORS_RANGE * 1.1:
            print("On the target, sir!")
            break

        if robot.free_space_ahead < robot.SENSORS_RANGE:
            print("Following the bondary until victory, sir!")
            boundary.follow_till_exit()
            print("Leaving this boundary, sir!")

    robot.stop()
