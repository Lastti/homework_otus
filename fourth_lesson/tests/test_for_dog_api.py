import pytest
import requests

from fourth_lesson.src.dog_api import get_names_of_all_breeds, get_names_of_all_breeds_with_sub_breeds, \
    get_sub_breeds_of_the_breed, url_list


@pytest.mark.parametrize('url', url_list)
def test_check_availability_of_methods(url):
    response = requests.get(url)
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    assert response.json()['status'] == 'success'


# think about 51
@pytest.mark.parametrize('number', [1, 25, 50], ids=['minimum', 'valid', 'maximum'])
def test_get_random_number_of_images(number):
    response = requests.get(f'https://dog.ceo/api/breed/hound/images/random/{number}')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    result = len(response.json()['message'])
    assert result == number, f'Wrong number of entries. Actual result: {number}, expected: {result}'


@pytest.mark.parametrize('breed', get_names_of_all_breeds())
def test_get_all_breed_images(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    message = response.json()['message']
    for image in message:
        assert f'{breed}' in image, f'Wrong breed image: {image} in {breed} response'


@pytest.mark.parametrize('breed', get_names_of_all_breeds_with_sub_breeds())
def test_get_sub_breed_list(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/list')
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    message = response.json()['message']
    assert message != [], f'There is no sub breeds for this breed: {breed}'


@pytest.mark.parametrize('breed', get_names_of_all_breeds_with_sub_breeds())
def test_get_all_sub_breed_images(breed):
    sub_breeds = get_sub_breeds_of_the_breed(breed)
    for sub_breed in sub_breeds:
        response = requests.get(f'https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random')
        assert response.ok, f'Response status code: {response.status_code} is not successful'
        image = response.json()['message']
        assert f'{breed}' in image and f'{sub_breed}' in image, f'Wrong image: {image} in {breed} breed ' \
                                                                f'with {sub_breed} sub breed response'
