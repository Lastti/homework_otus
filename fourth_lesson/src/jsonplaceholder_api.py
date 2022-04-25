base_url = 'https://jsonplaceholder.typicode.com'
posts_endpoint = base_url + '/posts'

main_posts_schema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'},
        }
    }
}

single_post_schema = {
    'type': 'object',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
    }
}

comments_schema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'postId': {'type': 'number'},
            'id': {'type': 'number'},
            'name': {'type': 'string'},
            'email': {'type': 'string'},
            'body': {'type': 'string'},
        }
    }
}
