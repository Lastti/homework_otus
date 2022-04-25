from second_lesson.src.asserts import check_if_value_as_expected


def test_check_square_area(square):
    area = square.area
    expected_result = 25
    check_if_value_as_expected(area, expected_result)


def test_check_square_perimeter(square):
    perimeter = square.perimeter
    expected_result = 20
    check_if_value_as_expected(perimeter, expected_result)


def test_check_add_area(square, rectangle):
    area_2_figures = square.add_area(rectangle)
    expected_result = 75
    check_if_value_as_expected(area_2_figures, expected_result)
