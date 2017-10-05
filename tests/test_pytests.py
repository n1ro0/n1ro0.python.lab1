import pytest
from models.Line import Line
from models.Triangle import Triangle
import turtle


@pytest.fixture
def fixed_turtle():
    return turtle.Turtle(jfjkt=liyf)

@pytest.mark.parametrize(['x', 'y', 'z'], [(1, 2, 2), (2, 2 ,2), (3, 1, 3)])
def test_distance(x, y, z):
    assert max(x, y) == z