import os

from dotenv import load_dotenv

load_dotenv()
url_book = os.getenv('URL_BOOK')
url_bot = os.getenv('URL_BOT')
url_cat = os.getenv('URL_CAT')
url_ip = os.getenv('IP_URL')
url_ip_location = os.getenv('IP_LOCATION')
url_wether = os.getenv('WETHER_URL')
key = os.getenv('KEYWETHER')
admin = os.getenv('admin')

url = f'https://api.telegram.org/bot{url_bot}/'
