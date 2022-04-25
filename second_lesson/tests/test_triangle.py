from second_lesson.src.asserts import check_if_value_as_expected


def test_check_triangle_area(triangle):
    area = triangle.area
    expected_result = 7.5
    check_if_value_as_expected(area, expected_result)


def test_check_triangle_perimeter(triangle):
    perimeter = triangle.perimeter
    expected_result = 15
    check_if_value_as_expected(perimeter, expected_result)


def test_check_add_area(triangle, circle):
    area_2_figures = triangle.add_area(circle)
    expected_result = 86.0
    check_if_value_as_expected(area_2_figures, expected_result)
