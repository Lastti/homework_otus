from second_lesson.src.asserts import check_if_value_as_expected


def test_check_circle_area(circle):
    area = circle.area
    expected_result = 78.5
    check_if_value_as_expected(area, expected_result)


def test_check_circle_perimeter(circle):
    perimeter = circle.perimeter
    expected_result = 31.42
    check_if_value_as_expected(perimeter, expected_result)


def test_check_add_area(circle, square):
    area_2_figures = circle.add_area(square)
    expected_result = 103.5
    check_if_value_as_expected(area_2_figures, expected_result)
