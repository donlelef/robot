from Point2D import Point2D

class Line2D(object):
    """ Represents a straight line in a 2D space """
    a = b = c = None

    def __init__(self, a, b, c):
        """ Creates a new line with equation ax + by + c = 0 """
        self.a = a
        self.b = b
        self.c = c

    def contains_point(self, point, tolerance):
        """ Checks whether a point lays on this line or not, with a given tolerance """
        return abs(self.a * point.x + self.b * point.y + self.c) < tolerance
    
    def __str__(self):
        """ Returns the equation of this line in the space """
        if self.b == 0:
            return "y = {.2f}x + {.2f}".format(-self.a, -self.c)
        else :
            return "{.2f}x + {.2f}y + {.2f} = 0".format(self.a, self.b, self.c)

    @classmethod
    def from_two_points(cls, p1, p2):
        """ Returns the instance of line passing through the given points """
        if p1.distance_from(p2) == 0:
            raise Exception("From one point infinite lines pass")
        if p1.x != p2.x:
                    m = (p2.y - p1.y) / (p2.x - p1.x)
                    q = (-1 * m * p1.x) + p1.y
                    return cls.from_explicit_form(m, q)
        else:
            return cls(1, 0, - p1.x)

    @classmethod
    def from_explicit_form(cls, m, q):
        """ Returns a new line with a given slope """
        return cls(-m, 1, -q)

    @classmethod
    def are_collinear(cls, p1, p2, p3, tolerance):
        """ Checks whether three points belong to the same line """
        return cls.from_two_points(p1, p2).contains_point(p3, tolerance)

