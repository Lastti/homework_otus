from second_lesson.src.figure import Figure


class Triangle(Figure):

    def check_triangle_sides(self, a, b, c):
        max_side = max(a, b, c)
        min_side = min(a, b, c)
        other_side = (a + b + c) - max_side - min_side
        if max_side >= min_side + other_side:
            raise ValueError('Triangle cannot be created with this sides')

    def __init__(self, a, b, c):
        self.check_triangle_sides(a, b, c)
        self.name = 'Triangle'
        self.side1 = a
        self.side2 = b
        self.side3 = c

    @property
    def area(self):
        return self.perimeter / 2

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def add_area(self, figure):
        return self.add_two_figures_area(figure)
