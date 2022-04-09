import json
from csv import DictReader
from itertools import cycle

with open("../third_lesson/files/users.json", "r") as f:
    users_list = []
    users = json.loads(f.read())

    for user in users:
        index = user['index']
        users_list.append({'name': user['name'], 'gender': user['gender'], 'address': user['address'],
                           'age': user['age'], 'books': []})

with open('../third_lesson/files/books.csv', 'r') as f:
    books = DictReader(f)
    books_list = []

    for book in books:
        books_list.append({'title': book['Title'], 'author': book['Author'], 'pages': book['Pages'],
                           'genre': book['Genre']})

iter_books = (book for book in books_list)
for u in cycle(users_list):
    try:
        print(u['name'], u['books'])
        u['books'].append(next(iter_books))
    except StopIteration:
        break

with open('result.json', 'w') as f:
    s = json.dumps(users_list, indent=4)
    f.write(s)
