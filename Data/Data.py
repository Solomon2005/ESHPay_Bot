import os
import csv

from settings.setings import url_bot, url
from utils.utils import send_message_text


def chack_Notes_csv():
    if not os.path.exists('dataNotes.csv'):
        with open('dataNotes.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID','Name', 'Notes'])

def add_new_notes(message):
    try:
        Notes = message['text'][9:]
        name = message['chat']['username']
        chat_id = message['chat']['id']
        new_row=[chat_id, name, Notes]
        with open('dataNotes.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)
    except ValueError:
        send_message_text(message['chat']['id'], "Заметка не получилась")

def get_notes_csv(callback):
    chat_id = callback['from']['id']
    with open('dataNotes.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'] == str(chat_id):
                send_message_text(chat_id, row['Notes'])



