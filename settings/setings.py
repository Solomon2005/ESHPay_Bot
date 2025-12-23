import os

from dotenv import load_dotenv

load_dotenv()
url_book = os.getenv('URL_BOOK')
url_bot = os.getenv('URL_BOT')
url_cat = os.getenv('URL_CAT')
url_wether = os.getenv('2gisWETHER_URL')
key = os.getenv('KEYWETHER')
key_wether = os.getenv('2giskew')
url = f'https://api.telegram.org/bot{url_bot}/'
