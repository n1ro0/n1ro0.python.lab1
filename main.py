import turtle
from models.TriangleSerpinskogo import TriangleSerpinskogo as TS


t = turtle.Turtle()
#ts = TS(t, (-300, -200), (0, 250), (300, -200)).draw()
ts = TS(t, (-300, -200), (0, 250), (300, -200), conter_clockwise=True).draw_reverse()
input()