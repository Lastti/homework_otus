from math import pi

from src.figure import Figure


class Circle(Figure):

    def __init__(self, a):
        self.name = 'Circle'
        self.radius = a

    @property
    def area(self):
        return round(pi, 2) * (self.radius ** 2)

    @property
    def perimeter(self):
        return round((2 * pi * self.radius), 2)

    def add_area(self, figure):
        return self.add_two_figures_area(figure)
