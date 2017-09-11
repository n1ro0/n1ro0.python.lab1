from models.GeometricFigure import GeometricFigure
import math

class Line(GeometricFigure):

    def __init__(self, turtle, point1, point2, color="black"):
        self.turtle = turtle
        self.point1 = point1
        self.point2 = point2
        self.color = color

    @property
    def turtle(self):
        return self._turtle

    @property
    def point1(self):
        return self._point1

    @property
    def point2(self):
        return self._point2

    @property
    def color(self):
        return self._color

    @property
    def middle_point(self):
        return ((self.point1[0] + self.point2[0]) / 2, (self.point1[1] + self.point2[1]) / 2)

    @property
    def distance(self):
        if abs(self.point1[0]) > abs(self.point2[0]):
            dist_x = abs(self.point1[0] - self.point2[0])
        else:
            dist_x = abs(self.point2[0] - self.point1[0])
        if abs(self.point1[1]) > abs(self.point2[1]):
            dist_y = abs(self.point1[1] - self.point2[1])
        else:
            dist_y = abs(self.point2[1] - self.point1[1])
        return math.sqrt(dist_x ** 2 + dist_y ** 2)

    @turtle.setter
    def turtle(self, value):
        self._turtle = value

    @point1.setter
    def point1(self, value):
        self._point1 = value

    @point2.setter
    def point2(self, value):
        self._point2 = value

    @color.setter
    def color(self, value):
        self._color = value

    def draw(self):
        self.turtle.pencolor(self.color)
        # first option
        self.turtle.penup()
        self.turtle.goto(self.point1)
        self.turtle.pendown()
        self.turtle.goto(self.point2)
        #second and shorter option
        #t.setposition(point1)
        #t.goto(point2)