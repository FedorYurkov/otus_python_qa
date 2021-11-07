# -*- coding: utf-8 -*-
import pytest

from hw2.src.Circle import Circle
from hw2.src.Square import Square


def test_circle_name():
    circle = Circle(10)
    assert circle.name == "Circle"


circle_area = [(0, 0),
               (1, 0.7853981633974483),
               (5, 19.634954084936208)
               ]


@pytest.mark.parametrize("diameter, area", circle_area)
def test_circle_area(diameter, area):
    circle = Circle(diameter)
    assert circle.area == area


circle_perimeter = [(0, 0),
                    (1, 3.141592653589793),
                    (5, 15.707963267948966)
                    ]


@pytest.mark.parametrize("diameter, perimeter", circle_perimeter)
def test_circle_area(diameter, perimeter):
    circle = Circle(diameter)
    assert circle.perimeter == perimeter


def test_circle_add_area():
    circle = Circle(5)
    square = Square(10)

    assert circle.add_area(square) == 119.634954084936208
