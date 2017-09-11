from models.Triangle import Triangle

class TriangleSerpinskogo(Triangle):

    def __init__(self, turtle, point1, point2, point3, outer_fill_color="black", inner_fill_color="white",
                 min_side_length = 10, conter_clockwise = False, border_color1="black", border_color2="black", border_color3="black"):
        super().__init__(turtle, point1, point2, point3, outer_fill_color,
                 border_color1, border_color2, border_color3)
        self.inner_fill_color = inner_fill_color
        self.min_side_length = min_side_length
        self.conter_clockwise = conter_clockwise

    @property
    def inner_fill_color(self):
        return self._inner_fill_color

    @property
    def min_side_length(self):
        return self._min_side_length

    @property
    def conter_clockwise(self):
        return self._conter_clockwise

    @inner_fill_color.setter
    def inner_fill_color(self, value):
        self._inner_fill_color = value

    @min_side_length.setter
    def min_side_length(self, value):
        self._min_side_length = value

    @conter_clockwise.setter
    def conter_clockwise(self, value):
        self._conter_clockwise = value

    def _draw_helper(self, triangle):
        if triangle.low_distance(self.min_side_length):
          return
        triangle.fill_color = self.inner_fill_color
        middle_points = triangle.middle_points
        triangle.draw_from_points(middle_points)
        triangle1 = Triangle(self.turtle, triangle.point1, middle_points[0], middle_points[2])
        triangle2 = Triangle(self.turtle, middle_points[0], triangle.point2, middle_points[1])
        triangle3 = Triangle(self.turtle, middle_points[2], middle_points[1], triangle.point3)
        if self.conter_clockwise == False:
            self._draw_helper(triangle1)
            self._draw_helper(triangle2)
            self._draw_helper(triangle3)
        else:
            self._draw_helper(triangle3)
            self._draw_helper(triangle2)
            self._draw_helper(triangle1)

    def draw(self):
        super().draw()
        self._draw_helper(Triangle(self.turtle, self.point1, self.point2, self.point3))

    def _draw_reverse_helper(self, triangle):
        if triangle.low_distance(self.min_side_length):
          return
        triangle.fill_color = self.inner_fill_color
        middle_points = triangle.middle_points

        triangle1 = Triangle(self.turtle, triangle.point1, middle_points[0], middle_points[2])
        triangle2 = Triangle(self.turtle, middle_points[0], triangle.point2, middle_points[1])
        triangle3 = Triangle(self.turtle, middle_points[2], middle_points[1], triangle.point3)
        if self.conter_clockwise == False:
            self._draw_reverse_helper(triangle1)
            self._draw_reverse_helper(triangle2)
            self._draw_reverse_helper(triangle3)
        else:
            self._draw_reverse_helper(triangle3)
            self._draw_reverse_helper(triangle2)
            self._draw_reverse_helper(triangle1)
        triangle.draw_from_points(middle_points)

    def draw_reverse(self):
        super().draw()
        self._draw_reverse_helper(Triangle(self.turtle, self.point1, self.point2, self.point3))


