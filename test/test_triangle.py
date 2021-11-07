# -*- coding: utf-8 -*-
import pytest

from src.Square import Square
from src.Triangle import Triangle


def test_triangle_name():
    triangle = Triangle(3, 4, 5)
    assert triangle.name == "Triangle"


triangle_area = [(1, 1, 1, 0.4330127018922193),
                 (3, 4, 5, 6)
                 ]


@pytest.mark.parametrize("side_1, side_2, side_3, area", triangle_area)
def test_triangle_area(side_1, side_2, side_3, area):
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.area == area


triangle_perimeter = [(1, 1, 1, 3),
                      (3, 4, 5, 12)
                      ]


@pytest.mark.parametrize("side_1, side_2, side_3, perimeter", triangle_perimeter)
def test_triangle_area(side_1, side_2, side_3, perimeter):
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.perimeter == perimeter


def test_triangle_add_area():
    triangle = Triangle(3, 4, 5)
    square = Square(5)

    assert triangle.add_area(square) == 31
