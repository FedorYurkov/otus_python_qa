# -*- coding: utf-8 -*-
import math

from src.Figure import Figure


class Triangle(Figure):

    name = "Triangle"

    def __init__(self, side_1, side_2, side_3):
        for item in [side_1, side_2, side_3]:
            if type(item) not in [int, float]:
                raise ValueError("Передано не число.")

        max_side = max(side_1, side_2, side_3)
        if max_side < (side_1 + side_2 + side_3) - max_side:
            self.side_1 = side_1
            self.side_2 = side_2
            self.side_3 = side_3
        else:
            raise ValueError("Не возможно создать треугольник")

    @property
    def area(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        return math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))

    @property
    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3
