import requests
import json

from book_inf.Get_rest_inf import get_inf_book
from settings.setings import url_bot, url
from book_inf.Get_rest_inf import get_inf_book
from body.batton import *



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
        if 'Заметка:' in text:
            from Data.Data import add_new_notes
            add_new_notes(message)
            send_message_text(chat_id,'Заметка сохранена')
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
        send_message_text(chat_id,"Напишите ваши заметки к книгам через:"
                                  '\n"Заметка:_"')
    if text == "btnCats":
        send_message_text(chat_id,'Коты')
    if text == "btnLocation":
        send_message_text(chat_id, 'Локация')
    if text == "MYbtnNotes":
        from Data.Data import get_notes_csv
        try:
            send_message_text(chat_id, 'Мои Заметки'
                                       '\n ---------------- ')
            get_notes_csv(callback)
            send_message_text(chat_id, '---------------- ')
        except:
            send_message_text(chat_id,"Что-то сломалось")

    if text == 'fantasy':
        get_inf_book('fantasy',10)



