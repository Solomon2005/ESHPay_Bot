import requests
import json
import os
import csv

from settings.setings import url_bot
from utils.utils import send_message_text
from utils.utils import get_chak_mess

url = f'https://api.telegram.org/bot{url_bot}/'


def chack_Notes_csv():
    if not os.path.exists('dataNotes.csv'):
        with open('dataNotes.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID','Name', 'Notes'])

def add_new_notes():
    if not update_response['result']:
        return
    last_msg = update_response['result'][-1]
    if 'message' not in last_msg:
        return

    try:
        Notes = last_msg['message']['text']
        name = last_msg['message']['chat']['username']
        chat_id = last_msg['message']['chat']['id']
        new_row=[chat_id, name, Notes]
        with open('dataNotes.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)
    except ValueError:
        send_message_text(last_msg['message']['chat']['id'], "Иди нахуй")

