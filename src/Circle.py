# -*- coding: utf-8 -*-
from math import pi

from src.Figure import Figure


class Circle(Figure):

    name = "Circle"

    def __init__(self, diameter):
        if type(diameter) not in [int, float]:
            raise ValueError("Передано не число.")
        self.diameter = diameter

    @property
    def area(self):
        return pi * (self.diameter ** 2) / 4

    @property
    def perimeter(self):
        return pi * self.diameter
