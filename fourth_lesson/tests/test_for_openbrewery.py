import pytest
import requests
from jsonschema import validate

from fourth_lesson.src.openbrewerydb_api import base_url, main_schema, get_all_breweries, single_schema, \
    filter_options_for_brewery


def test_get_all_breweries():
    response = requests.get(base_url)
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    response = response.json()
    validate(instance=response, schema=main_schema)


@pytest.mark.parametrize('method, my_filter, exp_result', filter_options_for_brewery,
                         ids=['by_city', 'by_dist', 'by_name', 'by_state', 'by_postal'])
def test_check_filtration_methods(method, my_filter, exp_result):
    response = requests.get(f'{base_url}?{method}={my_filter}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    id = response.json()[0]['id']
    assert id == exp_result, f'Wrong result of breweries filtration by {method}. ' \
                             f'Expected id: {exp_result}, actual id: {id}'


@pytest.mark.parametrize('my_filter', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar',
                                       'contract',
                                       pytest.param('proprietor', marks=
                                       pytest.mark.skip(reason='"proprietor" should be fixed')),
                                       'closed'])
def test_check_filtration_by_type(my_filter):
    response = requests.get(f'{base_url}?by_type={my_filter}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    brewery_type = response.json()[0]['brewery_type']
    assert brewery_type == my_filter, f'Wrong result of breweries filtration by type. ' \
                                      f'Expected brewery type: {my_filter}, actual brewery type: {brewery_type}'


@pytest.mark.parametrize('brewery_id', get_all_breweries())
def test_get_single_brewery(brewery_id):
    response = requests.get(f'{base_url}/{brewery_id}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    response = response.json()
    validate(instance=response, schema=single_schema)


@pytest.mark.parametrize('search_type',
                         [pytest.param('search', marks=pytest.mark.skip(reason='search method should be fixed')),
                          'autocomplete'])
def test_search_breweries(search_type):
    search_text = 'dog'
    response = requests.get(f'{base_url}/{search_type}?query={search_text}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    response = response.json()
    for i in response:
        name = i['name']
        assert f'{search_text}' in name.lower(), f'Wrong search results: "{search_text}" not found in search results'
