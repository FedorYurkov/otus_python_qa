# -*- coding: utf-8 -*-
from hw2.src.Figure import Figure


class Rectangle(Figure):

    name = "Rectangle"

    def __init__(self, side_1, side_2):
        for item in [side_1, side_2]:
            if type(item) not in [int, float]:
                raise ValueError("Передано не число.")

        self.side_1 = side_1
        self.side_2 = side_2

    @property
    def area(self):
        return self.side_1 * self.side_2

    @property
    def perimeter(self):
        return (self.side_1 + self.side_2) * 2
