import requests
import json
import os
import csv

from settings.setings import url_bot

url = f'https://api.telegram.org/bot{url_bot}/'

def get_chak_mess():
    update_response = requests.get(f'{url}{"getUpdates"}').json()
    print(json.dumps(update_response, indent=4,  ensure_ascii=False))

def chack_Notes_csv():
    if not os.path.exists('dataNotes.csv'):
        with open('dataNotes.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID','Name', 'Notes'])

