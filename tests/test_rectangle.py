from src.asserts import check_if_value_as_expected


def test_check_rectangle_area(rectangle):
    area = rectangle.area
    expected_result = 50
    check_if_value_as_expected(area, expected_result)


def test_check_rectangle_perimeter(rectangle):
    perimeter = rectangle.perimeter
    expected_result = 30
    check_if_value_as_expected(perimeter, expected_result)


def test_check_add_area(rectangle, triangle):
    area_2_figures = rectangle.add_area(triangle)
    expected_result = 57.5
    check_if_value_as_expected(area_2_figures, expected_result)
