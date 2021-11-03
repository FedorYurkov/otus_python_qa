# -*- coding: utf-8 -*-
from src.Figure import Figure


class Square(Figure):

    name = "Square"

    def __init__(self, side):
        if type(side) not in [int, float]:
            raise ValueError("Передано не число.")
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4
