from models.GeometricFigure import GeometricFigure
from models.Line import Line

class Triangle(GeometricFigure):

    def __init__(self, turtle, point1, point2, point3, fill_color="black",
                 border_color1="black", border_color2="black", border_color3="black"):
        self.turtle = turtle
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.fill_color = fill_color
        self.border_color1 = border_color1
        self.border_color2 = border_color2
        self.border_color3 = border_color3

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
    def point3(self):
        return self._point3

    @property
    def fill_color(self):
        return self._fill_color

    @property
    def border_color1(self):
        return self._border_color1

    @property
    def border_color2(self):
        return self._border_color2

    @property
    def border_color3(self):
        return self._border_color3

    @property
    def line1(self):
        return Line(self.turtle, self.point1, self.point2, self.border_color1)

    @property
    def line2(self):
        return Line(self.turtle, self.point2, self.point3, self.border_color2)

    @property
    def line3(self):
        return Line(self.turtle, self.point3, self.point1, self.border_color3)

    @property
    def middle_points(self):
        return (self.line1.middle_point, self.line2.middle_point, self.line3.middle_point)

    @turtle.setter
    def turtle(self, value):
        self._turtle = value

    @point1.setter
    def point1(self, value):
        self._point1 = value

    @point2.setter
    def point2(self, value):
        self._point2 = value

    @point3.setter
    def point3(self, value):
        self._point3 = value

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = value

    @border_color1.setter
    def border_color1(self, value):
        self._border_color1 = value

    @border_color2.setter
    def border_color2(self, value):
        self._border_color2 = value

    @border_color3.setter
    def border_color3(self, value):
        self._border_color3 = value

    def low_distance(self, distance):
        if self.line1.distance < distance or self.line2.distance < distance or self.line3.distance < distance:
            return True
        return False

    def draw(self):
        self.turtle.fillcolor(self.fill_color)
        self.turtle.begin_fill()
        self.line1.draw()
        self.line2.draw()
        self.line3.draw()
        self.turtle.end_fill()

    def draw_from_points(self, points):
        self.turtle.fillcolor(self.fill_color)
        self.turtle.begin_fill()
        Line(self.turtle, points[0], points[1]).draw()
        Line(self.turtle, points[1], points[2]).draw()
        Line(self.turtle, points[2], points[0]).draw()
        self.turtle.end_fill()