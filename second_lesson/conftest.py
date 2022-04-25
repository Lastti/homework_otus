import pytest

from second_lesson.src.circle import Circle
from second_lesson.src.rectangle import Rectangle
from second_lesson.src.square import Square
from second_lesson.src.triangle import Triangle


@pytest.fixture
def triangle():
    triangle = Triangle(4, 5, 6)
    yield triangle
    del triangle


@pytest.fixture
def rectangle():
    rectangle = Rectangle(10, 5)
    yield rectangle
    del rectangle


@pytest.fixture
def square():
    square = Square(5)
    yield square
    del square


@pytest.fixture
def circle():
    circle = Circle(5)
    yield circle
    del circle
