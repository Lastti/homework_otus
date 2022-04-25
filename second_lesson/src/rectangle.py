from second_lesson.src.figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.name = 'Rectangle'
        self.side1 = a
        self.side2 = b

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return (self.side1 + self.side2) * 2

    def add_area(self, figure):
        return self.add_two_figures_area(figure)
