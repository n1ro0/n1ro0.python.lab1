import turtle
import math
from models.Line import Line
from models.TriangleSerpinskogo import TriangleSerpinskogo as TS

def draw_line(t, point1, point2, color="black"):
    t.pencolor(color)

    #first option
    t.penup()
    t.goto(point1)
    t.pendown()
    t.goto(point2)

    #second and shorter option
    #t.setposition(point1)
    #t.goto(point2)

def draw_triangle(t, points=None, fill_color="black", border_color1="black", border_color2="black", border_color3="black"):
    if points == None or len(points) != 3:
        points = ((0, 0), (0, 100), (100, 0))
    t.fillcolor(fill_color)
    t.begin_fill()
    Line(t, points[0], points[1], border_color1).draw()
    Line(t, points[1], points[2], border_color1).draw()
    Line(t, points[2], points[0], border_color1).draw()
    t.end_fill()

def middle_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def triangle_middle_points(points):
    return (middle_point(points[0], points[1]), middle_point(points[1], points[2]), middle_point(points[2], points[0]))

def low_distance(points):
    if abs(points[0][0]) > abs(points[1][0]):
        dist_x = abs(points[0][0] - points[1][0])
    else:
        dist_x = abs(points[1][0] - points[0][0])
    if abs(points[0][1]) > abs(points[1][1]):
        dist_y = abs(points[0][1] - points[1][1])
    else:
        dist_y = abs(points[1][1] - points[0][1])
    dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
    if(dist < 3):
        return True
    return False

def draw_triangle_serpinskogo(t, points = None, outer_fill_color="black", inner_fill_color="white"):
    if points == None or len(points) != 3:
        points = ((0, 0), (0, 100), (100, 0))
    if low_distance(points):
        return
    draw_triangle(t, points, fill_color=outer_fill_color)
    middle_points = triangle_middle_points(points)
    draw_triangle(t, middle_points, fill_color=inner_fill_color)
    first_triangle_points = (points[0], middle_points[0], middle_points[2])
    second_triangle_points = (middle_points[0], points[1],  middle_points[1])
    third_triangle_points = (middle_points[1], points[2], middle_points[2])
    draw_triangle_serpinskogo(t, first_triangle_points, outer_fill_color, inner_fill_color)
    draw_triangle_serpinskogo(t, second_triangle_points, outer_fill_color, inner_fill_color)
    draw_triangle_serpinskogo(t, third_triangle_points, outer_fill_color, inner_fill_color)

def draw_triangle_serpinskogo_other(t, points = None, outer_fill_color="black", inner_fill_color="white"):
    if points == None or len(points) != 3:
        points = ((0, 0), (0, 100), (100, 0))
    if low_distance(points):
        return
    draw_triangle(t, points, fill_color=outer_fill_color)
    draw_triangle_serpinskogo_other_helper(t, points, inner_fill_color)

def draw_triangle_serpinskogo_other_helper(t, points = None, inner_fill_color="white"):
    if low_distance(points):
        return
    middle_points = triangle_middle_points(points)
    draw_triangle(t, middle_points, fill_color=inner_fill_color)
    first_triangle_points = (points[0], middle_points[0], middle_points[2])
    second_triangle_points = (middle_points[0], points[1],  middle_points[1])
    third_triangle_points = (middle_points[1], points[2], middle_points[2])
    draw_triangle_serpinskogo_other_helper(t, first_triangle_points, inner_fill_color)
    draw_triangle_serpinskogo_other_helper(t, second_triangle_points, inner_fill_color)
    draw_triangle_serpinskogo_other_helper(t, third_triangle_points, inner_fill_color)



t = turtle.Turtle()
#draw_triangle(a, ((0, 0), (0, 100), (100, 0)), fill_color="white")
#draw_triangle_serpinskogo_other(a, ((-300, -200), (0, 250), (300, -200)))
ts = TS(t, (-300, -200), (0, 250), (300, -200)).draw()
ts = TS(t, (-300, -200), (0, 250), (300, -200), conter_clockwise=True).draw_reverse()
input()


