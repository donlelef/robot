from pymorse import Morse

from crash_generator.boundary_follow import BoundaryFollower
from crash_generator.bug2_exit_condition import Bug2ExitCondition
from crash_generator.motion_to_goal import MotionToGoal
from crash_generator.robot import Robot
from crash_generator.simple_motion import SimpleMotion
from crash_generator.trilateration.trilateration import Trilaterator
from crash_generator.trilateration.trilateration_solution import TrilaterationSolver

with Morse() as sim:
    robot = Robot(sim.robot, sim)

    '''start tmp'''
    trilaterator = Trilaterator(robot, TrilaterationSolver())
    motion = SimpleMotion(robot, 1, 1, trilaterator)
    motion.go_until_exit()
    print(trilaterator.goal)

    # boundary = BoundaryFollower(robot, trilaterator)

    # motion.go_until_exit()
    # print('Trilaterating or crashing, sir!')
    # if trilaterator.goal is None:
    #     print('Wall detected. Following the boundary while trilaterating, sir!')
    #     boundary.follow_till_exit()
    # robot.stop()
    # goal = trilaterator.goal
    # print('Target acquired at {}... going for conquer, sir!'.format(goal))
    # '''end tmp'''
    #
    # motion = MotionToGoal(robot, goal)
    # boundary = BoundaryFollower(robot, Bug2ExitCondition(robot, goal))
    #
    # while True:
    #
    #     motion.go_until_target_or_obstacle()
    #
    #     if robot.distance_to_target < 2.5:
    #         print("On the target, sir!")
    #         break
    #
    #     if robot.free_space_ahead < robot.SENSORS_RANGE:
    #         print("Following the bondary until victory, sir!")
    #         boundary.follow_till_exit()
    #         print("Leaving this boundary, sir!")
    #
    # robot.stop()
