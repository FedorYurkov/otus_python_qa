# -*- coding: utf-8 -*-
import pytest

from hw2.src.Square import Square


def test_square_name():
    square = Square(10)
    assert square.name == "Square"


square_area = [(0, 0),
               (1, 1),
               (5, 25)
               ]


@pytest.mark.parametrize("side, area", square_area)
def test_square_area(side, area):
    square = Square(side)
    assert square.area == area


square_perimeter = [(0, 0),
                    (1, 4),
                    (5, 20)
                    ]


@pytest.mark.parametrize("side, perimeter", square_perimeter)
def test_square_area(side, perimeter):
    square = Square(side)
    assert square.perimeter == perimeter


def test_square_add_area():
    square_1 = Square(10)
    square_2 = Square(5)

    assert square_1.add_area(square_2) == 125
