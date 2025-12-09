import requests
import json
from settings.setings import url_bot
from body.batton import *


url = f'https://api.telegram.org/bot{url_bot}/'

def get_chak_mess():
    update_response = requests.get(f'{url}{"getUpdates"}').json()
    print(json.dumps(update_response, indent=4,  ensure_ascii=False))

def send_message_text(chat_id, text):
    update_response = requests.get(f'{url}{"getUpdates"}').json()
    params = {
        'chat_id': chat_id,
        'text': text
    }
    return requests.post(f'{url}{'sendMessage'}', params=params)

def messages(message):
    update_response = requests.get(f'{url}{"getUpdates"}').json()
    chat_id = message['chat']['id']
    text = message['text']

    if text == '/start':
        start_button_message(chat_id)
    if text == '/help':
        send_message_text(chat_id,'помощь')

def buttom_message(callback):
    update_response = requests.get(f'{url}{"getUpdates"}').json()
    chat_id = callback['from']['id']
    text = callback['data']
    if text == 'btnSearch':
        Search_genre_button_message(chat_id)
    if text == "btnNotes":
        send_message_text(chat_id,"Заметки")
    if text == "btnCats":
        send_message_text(chat_id,'Коты')
    if text == "btnLocation":
        send_message_text(chat_id, 'Локация')




