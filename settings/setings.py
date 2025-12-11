import os

from dotenv import load_dotenv

load_dotenv()
url_book = os.getenv('URL_BOOK')
url_bot = os.getenv('URL_BOT')

url = f'https://api.telegram.org/bot{url_bot}/'