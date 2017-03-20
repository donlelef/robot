#! /usr/bin/env python3

from time import sleep

class Position2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)

    @staticmethod
    def from_morse(morse_position):
        x = morse_position['x']
        y = morse_position['y']
        return Position2D(x, y)


class Robot:
    
    def __init__(self, morse_robot):
        self.morse_object = morse_robot

    @property
    def position(self):
        return Position2D.from_morse(self.morse_object.pose.get())

    @property
    def distance_to_target(self):
        return self.morse_object.prox.get()['near_robots']['GOAL']

    @property
    def orientation(self):
        return self.morse_object.pose.get()['yaw']

    def set_velocity(self, linear, angular):
        self.morse_object.motion.publish({'v': linear, 'w': angular})
        return self

    def stop(self):
        self.set_velocity(0, 0)
        return self

    def stop_after(self, seconds):
        sleep(seconds)
        self.stop()
        return self