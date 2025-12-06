import requests
from bs4 import BeautifulSoup
from time import sleep
from setings import url_cards

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def get_url_card():
    url = url_cards

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all("li", class_="search-business-snippet-view__content")
    for i in data:
        card_url = ""
        yield card_url