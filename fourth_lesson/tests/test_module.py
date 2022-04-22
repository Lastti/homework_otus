import requests


def test_check_url(base_url, exp_status_code):
    response = requests.get(base_url)
    print(base_url, exp_status_code)
    assert response.status_code == exp_status_code, f'Wrong status code: {response.status_code}, ' \
                                                    f'expected: {exp_status_code}'
