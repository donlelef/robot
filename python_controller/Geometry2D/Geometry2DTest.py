import unittest
from Geometry2D import Point2D, Line2D

class Test_Geometry2D(unittest.TestCase):
    
    p1 = p2 = p3 = p4 = line = None

    def setUp(self):
        p1 = Point2D(0, 0)
        p2 = Point2D(1, 1)
        p3 = Point2D(4, 4)
        p4 = Point2D(0, 1)
        return super(Test_Geometry2D, self).setUp()

    def points_distance(self):
        print(str(p1))

if __name__ == '__main__':
    unittest.main()
