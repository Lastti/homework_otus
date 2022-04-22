import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        help='This is request url'
    )

    parser.addoption(
        '--status_code',
        default=200,
        help='This is expected status code'
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def exp_status_code(request):
    return int(request.config.getoption('--status_code'))
