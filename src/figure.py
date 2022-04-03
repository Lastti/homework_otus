from abc import abstractmethod


class Figure:

    @property
    @abstractmethod
    def area(self):
        pass

    def add_two_figures_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f'Class {figure.name} is no subclass of a Figure')
        return self.area + figure.area
