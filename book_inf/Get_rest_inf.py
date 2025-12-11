import requests
import json
from settings.setings import url_book


def get_inf_book(query,limit):
    params = {
        "q": query,
        'limit' : limit,
        'fields': 'title,author_name',
        "language": 'rus'
    }

    response = requests.get(url_book, params=params)

    if response.status_code == 200:
        books = response.json()['docs']

        all_book=[]
        for book in books:
            title = book.get('title')
            authors_name = book.get('author_name')

            all_book.append({
                'title':title,
                'author_name':authors_name
            })
        return all_book
    else:
        print (response.status_code)
        return []
