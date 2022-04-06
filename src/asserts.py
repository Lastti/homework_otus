def check_if_value_as_expected(value, expected_result):
    assert value == expected_result, f'Wrong calculation. Actual result: {value} is not the same' \
                                     f' as expected: {expected_result}'
