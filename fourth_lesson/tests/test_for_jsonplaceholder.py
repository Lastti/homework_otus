import pytest
import requests
from jsonschema import validate

from fourth_lesson.src.jsonplaceholder_api import posts_endpoint, main_posts_schema, single_post_schema, comments_schema


def test_get_all_posts():
    response = requests.get(posts_endpoint)
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    validate(instance=response.json(), schema=main_posts_schema)


@pytest.mark.parametrize('id', [1, 50, 100], ids=['minimum', 'valid', 'maximum'])
def test_get_any_post(id):
    response = requests.get(f'{posts_endpoint}/{id}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    validate(instance=response.json(), schema=single_post_schema)


@pytest.mark.parametrize('id', ['one', 101], ids=['letter', 'invalid'])
def test_get_any_post_negative(id):
    response = requests.get(f'{posts_endpoint}/{id}')
    assert response.status_code == 404, f'Wrong status code: {response.status_code}, expected: 404'


@pytest.mark.parametrize('url', ['https://jsonplaceholder.typicode.com/comments?postId=1',
                                 'https://jsonplaceholder.typicode.com/posts/1/comments'])
def test_get_any_comment(url):
    response = requests.get(url)
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    validate(instance=response.json(), schema=comments_schema)


def test_add_new_post():
    user_id = 10
    payload = {
        "userId": user_id,
        "title": "some title",
        "body": "some text"
    }
    response = requests.post(posts_endpoint, json=payload)
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    validate(instance=response.json(), schema=single_post_schema)


def test_delete_post():
    id = 10
    response = requests.delete(f'{posts_endpoint}/{id}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
