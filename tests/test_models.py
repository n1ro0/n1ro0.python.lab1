import unittest
from unittest.mock import patch, ANY, sentinel




from models.Line import Line
from models.Triangle import Triangle
import turtle


class TestLineMethods(unittest.TestCase):

    def test_distance(self):
        line = Line(turtle.Turtle(), (0, 0), (0, 10))
        self.assertEqual(line.distance, 10)

    @patch('models.Triangle.Line')
    def test_line(self, line):
        tr = Triangle(turtle.Turtle(), sentinel.p1, (10, 10), (10, 0))
        x = tr.line3
        print(line.mock_calls)
        line.assert_called_once_with(ANY, tr.point3, sentinel.p1, tr.border_color3)

class TestTriangleMethods(unittest.TestCase):

    def test_line1(self):
        Triangle(turtle.Turtle(), (0, 0), (10, 10), (10, 0))
        line = Line(turtle.Turtle(), (0, 0), (0, 10))
        self.assertEqual(line.distance, 10)

if __name__ == '__main__':
    unittest.main()