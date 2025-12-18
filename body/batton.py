import requests
import json
from settings.setings import url_bot, url


def start_button_message(chat_id):
    keyboard = {
        'inline_keyboard': [
            [{"text": " Поиск", "callback_data": "btnSearch"}],
            [{"text": " Заметки", "callback_data": "btnNotes"}],
            [{"text": " Коты", "callback_data": "btnCats"}],
            [{"text": " Локация", "callback_data": "btnLocation"}]
        ]

    }

    params = {
        "chat_id": chat_id,
        "text": 'Привет, я бот Который поможет найти книги.'
                '\nЗапомню если тебе надо на какой странице '
                '\nв какой книге ты остановился',
        "reply_markup": json.dumps(keyboard)
    }
    return requests.post(f'{url}{"sendMessage"}', params=params)

def Search_genre_button_message(chat_id):
    keyboard = {
        'inline_keyboard': [
            [{"text": "Фантастика", "callback_data": "fantasy"}],#1
            [{"text": "Ужасы", "callback_data": "horror"}],#2
            [{"text": "Юмор", "callback_data": "humor"}],#3
            [{"text": "Мистика и детективы", "callback_data": "mystery_and_detective_stories"}],#4
            [{"text": "Научная фантастика", "callback_data": "science_fiction"}],#5
            [{"text": "Религия", "callback_data": "religion"}],#6
            [{"text": "Классика", "callback_data": "literature"}],#7
            [{"text": "Психология", "callback_data": "psychology"}],#8
            [{"text": "Программирование", "callback_data": "programming"}],#9
            [{"text": "Котята", "callback_data": "kittens"}]#10
        ]

    }

    params = {
        "chat_id": chat_id,
        "text": 'Выбери из каталога жанров',
        "reply_markup": json.dumps(keyboard)
    }
    return requests.post(f'{url}{"sendMessage"}', params=params)


def Notes_button_message(chat_id):
    keyboard = {
        'inline_keyboard': [
            [{"text": " Добавить Заметки", "callback_data": "addNotes"}],
            [{"text": " Мои Заметки", "callback_data": "MYbtnNotes"}]
        ]
    }

    params = {
        "chat_id": chat_id,
        "text": 'Кнопки для заметок',
        "reply_markup": json.dumps(keyboard)
    }
    return requests.post(f'{url}{"sendMessage"}', params=params)