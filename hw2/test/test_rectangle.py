# -*- coding: utf-8 -*-
import pytest

from hw2.src import Rectangle
from hw2.src.Square import Square


def test_rectangle_name():
    rectangle = Rectangle(10, 5)
    assert rectangle.name == "Rectangle"


rectangle_area = [(0, 1, 0),
                  (1, 2, 2)
                  ]


@pytest.mark.parametrize("side_1, side_2, area", rectangle_area)
def test_rectangle_area(side_1, side_2, area):
    rectangle = Rectangle(side_1, side_2)
    assert rectangle.area == area


rectangle_perimeter = [(1, 2, 6),
                       (5, 4, 18)]


@pytest.mark.parametrize("side_1, side_2, perimeter", rectangle_perimeter)
def test_rectangle_area(side_1, side_2, perimeter):
    rectangle = Rectangle(side_1, side_2)
    assert rectangle.perimeter == perimeter


def test_rectangle_add_area():
    rectangle = Rectangle(10, 5)
    square = Square(5)

    assert rectangle.add_area(square) == 75
