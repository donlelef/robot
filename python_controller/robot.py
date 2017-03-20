#! /usr/bin/env python3

from time import sleep
from position import Position2D

class Robot:

    morse_object = None
    
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

    @property
    def ahead_range(self):
        return self.morse_object.ir1.get()['range_list'][10]

    @property
    def at_left_range(self):
        return self.morse_object.ir2.get()['range_list'][10]

    @property
    def at_right_range(self):
        return self.morse_object.ir3.get()['range_list'][10]

    @property
    def back_range(self):
        return self.morse_object.ir4.get()['range_list'][10]

    def set_velocity(self, linear, angular):
        self.morse_object.motion.publish({'v': linear, 'w': angular})
        return self

    def set_angular_velocity(self, angular):
        self.morse_object.motion.publish({'w': angular})
        return self

    def rotate_of(self, degree, velocity):
        self.stop()
        delay = degree / velocity
        self.set_velocity(0, 1).stop_after(delay)

    def stop(self):
        self.set_velocity(0, 0)
        return self

    def stop_after(self, seconds):
        sleep(seconds)
        self.stop()
        return self