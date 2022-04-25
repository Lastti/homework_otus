from second_lesson.src.figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.name = 'Square'
        self.side = a

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4

    def add_area(self, figure):
        return self.add_two_figures_area(figure)
