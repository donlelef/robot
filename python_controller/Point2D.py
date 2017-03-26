import math

class Point2D:
    """ Represents a point in a 2D space """

    x = y = None

    def __init__(self, x, y):
        """ Creates a new point in space """
        self.x = x
        self.y = y

    def distance_from(self, other):
        """ Returns the distance between this point and another """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) 
        
    def is_close_to(self, other, tolerance):
        """ Returns whether or not this point is close to another, for a given tolerance """
        return self.distance_from(other) < tolerance

    def __add__(self, other):
        """ Adds this point to another """
        return  self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Subtract a point from this one """
        return self.__class__(self.x - other.x, self.y - other.y)

    def __str__(self):
        """ Returns a textual representation of this point """
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)

    @classmethod
    def from_morse(cls, morse_position):
        """ Returns an instance of this class from Morse position data structure """
        x = morse_position['x']
        y = morse_position['y']
        return cls(x, y)


