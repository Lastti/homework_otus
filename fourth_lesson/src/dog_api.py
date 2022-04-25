import requests

url_list = ['https://dog.ceo/api/breeds/list/all',
            'https://dog.ceo/api/breeds/image/random',
            'https://dog.ceo/api/breeds/image/random/3',
            'https://dog.ceo/api/breed/hound/images',
            'https://dog.ceo/api/breed/hound/images/random',
            'https://dog.ceo/api/breed/hound/images/random/3',
            'https://dog.ceo/api/breed/hound/list',
            'https://dog.ceo/api/breed/hound/afghan/images',
            'https://dog.ceo/api/breed/hound/afghan/images/random',
            'https://dog.ceo/api/breed/hound/afghan/images/random/3'
            ]


def get_names_of_all_breeds():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    message = response.json()['message']
    list_all_breeds = message.keys()
    return list_all_breeds


def get_names_of_all_breeds_with_sub_breeds():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    message = response.json()['message']
    list_breeds_with_sub_breeds = []
    for key, value in message.items():
        if value:
            list_breeds_with_sub_breeds.append(key)
    return list_breeds_with_sub_breeds


def get_sub_breeds_of_the_breed(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/list')
    assert response.ok
    sub_breed_list = response.json()['message']
    return sub_breed_list
