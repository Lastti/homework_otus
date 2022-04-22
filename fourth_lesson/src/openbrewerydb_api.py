import requests

main_schema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'name': {'type': 'string'},
            'brewery_type': {'type': 'string'},
            'street': {'type': ['string', 'null']},
            'address_2': {'type': ['string', 'null']},
            'address_3': {'type': ['null', 'string']},
            'city': {'type': 'string'},
            'state': {'type': 'string'},
            'county_province': {'type': ['null', 'string']},
            'postal_code': {'type': 'string'},
            'country': {'type': 'string'},
            'longitude': {'type': ['string', 'null']},
            'latitude': {'type': ['string', 'null']},
            'phone': {'type': ['string', 'null']},
            'website_url': {'type': ['string', 'null']},
            'updated_at': {'type': 'string'},
            'created_at': {'type': 'string'}
        }
    }
}

single_schema = {

    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'brewery_type': {'type': 'string'},
        'street': {'type': ['string', 'null']},
        'address_2': {'type': ['string', 'null']},
        'address_3': {'type': ['null', 'string']},
        'city': {'type': 'string'},
        'state': {'type': 'string'},
        'county_province': {'type': ['null', 'string']},
        'postal_code': {'type': 'string'},
        'country': {'type': 'string'},
        'longitude': {'type': ['string', 'null']},
        'latitude': {'type': ['string', 'null']},
        'phone': {'type': ['string', 'null']},
        'website_url': {'type': ['string', 'null']},
        'updated_at': {'type': 'string'},
        'created_at': {'type': 'string'}
    }
}

base_url = 'https://api.openbrewerydb.org/breweries'

filter_options_for_brewery = [('by_city', 'san_diego', 'circle-9-brewing-san-diego'),
                              ('by_dist', '38.8977,77.0365', 'incheonbrewery-jung-gu'),
                              ('by_name', 'cooper', '3cross-fermentation-cooperative-worcester'),
                              ('by_state', 'ohio', 'snow-belt-brew-chardon'),
                              ('by_postal', '44107', 'bottlehouse-brewery-lakewood')
                              ]


def get_all_breweries():
    response = requests.get(base_url)
    assert response.ok, f'Response status code: {response.status_code} is not successful'
    response = response.json()
    all_breweries_list = []
    for i in response:
        all_breweries_list.append(i['id'])
    return all_breweries_list
