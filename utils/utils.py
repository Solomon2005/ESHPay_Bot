import requests
import json
from settings.setings import url_bot
from body.batton import *


url = f'https://api.telegram.org/bot{url_bot}/'

def get_chak_mess(message):
    print(json.dumps(message, indent=4,  ensure_ascii=False))

def send_message_text(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text
    }
    return requests.post(f'{url}{'sendMessage'}', params=params)

def messages(message):
    chat_id = message['chat']['id']
    if "text" in message:
        text = message['text']
        if text == '/start':
            start_button_message(chat_id)
        if text == '/help':
            send_message_text(chat_id,'помощь')
    if 'photo' in message:
        send_message_text(chat_id,"нахуй мне твоё фото")
    if 'document' in message:
        send_message_text(chat_id,"Засунь себе свой документ")

def buttom_message(callback):
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



