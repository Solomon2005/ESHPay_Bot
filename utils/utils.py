import requests
import json
import csv
import time, datetime


from settings.setings import *
from book_inf.Get_rest_inf import get_inf_book
from body.batton import start_button_message, Search_genre_button_message, Notes_button_message
from utils.get_cats import get_img_cat

def get_id_admin():
    try:
        with open('config.json') as f:
            fson_object = json.load(f)
            admin_id =[]
            for item in fson_object:
                if 'ID' in item:
                    admin_id.append(item['ID'])
            return admin_id
    except:
        print("Проблема с id админа")

def get_json_data(object):
    with open('task.json') as f:
        json_object = json.load(f)
        for elem in json_object:
            if object in elem:
                return (elem[object])

def get_chak_mess(message):
    try:
        print(json.dumps(message, indent=4,  ensure_ascii=False))
    except:
        print("ошибка в проверки сообщения")

def send_message_text(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text
    }
    return requests.post(f'{url}{'sendMessage'}', params=params)

def send_admin_txt():
    admin = get_id_admin()
    url_file = f"{url}sendDocument"
    for chat_id in admin:
        with open('dataRESULT.txt', 'rb') as f:
            print(chat_id)
            files = {'document': f}
            params = {"chat_id": chat_id}
            file_resp = requests.post(url_file, params=params, files=files)
    with open('dataRESULT.txt', 'w', encoding='utf-8') as f:
        f.write('')

def get_RESULT_txt(response):
    with open('dataRESULT.txt','a', newline='', encoding='utf-8') as f:
        f.write(json.dumps(response, ensure_ascii=False))
        f.write('\n')

def send_to_all_from_csv():
    try:
        all_id = []
        with open('dataStart.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_id.append(row['ID'])
        uniq_id = set(all_id)
        text = get_text("text.txt")
        for chat_id in list(uniq_id):
            send_message_text(chat_id, text)
    except:
        print("Ошибка")

def get_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
    return first_line


def messages(message):
    chat_id = message['chat']['id']
    if "text" in message:
        text = message['text']
        if text == '/start':
            from data.data import add_new_Start
            start_button_message(chat_id)
            add_new_Start(message)
        if text == '/help':
            send_message_text(chat_id,'помощь')
        if 'Заметка:' in text:
            from data.data import add_new_notes
            add_new_notes(message)
            send_message_text(chat_id, 'Заметка сохранена')

        if 'Заметки:' in text:
            send_message_text(chat_id, 'Напиши "Заметка" в место "Заметки"')
    if 'photo' in message:
        send_message_text(chat_id,"нахуй мне твоё фото")
    if 'document' in message:
        send_message_text(chat_id,"Засунь себе свой документ")
    if 'location' in message:
        latitude = message['location']['latitude']
        longitude = message['location']['longitude']
        full_name = wether(latitude, longitude)
        text = f"Вы сейчас в {full_name}"
        send_message_text(chat_id, text,)
    if "sticker" in message:
        send_message_text(chat_id, "Не обрабатываем стикеры")


def wether(latitude,longitude):
    try:
        params = {
            "lat": latitude,
            "lon": longitude,
            "field": "items.point",
            "key": key_wether,
        }

        weather = requests.get(url_wether, params=params).json()
        full_name = weather["result"]["items"][0]["full_name"]
        return full_name
    except:
        print("Возможно закончились запросы")

def buttom_message(callback):
    chat_id = callback['from']['id']
    text = callback['data']
    if text == 'btnSearch':
        Search_genre_button_message(chat_id)
    #Заметки
    if text == "btnNotes":
        Notes_button_message(chat_id)
    if text == "addNotes":
        send_message_text(chat_id,"Напишите ваши заметки к книгам через:"
                '\n"Заметка:_"')
    if text == "DelNotes":
        send_message_text(chat_id,"Удалены")
    #Коты
    if text == "btnCats":
        get_img_cat(chat_id)
    if text == "btnLocation":
        send_message_text(chat_id, 'Отправь свою локацию')
    if text == "MYbtnNotes":
        from data.data import get_notes_csv
        try:
            send_message_text(chat_id, 'Мои Заметки'
                                       '\n ---------------- ')
            get_notes_csv(callback)
            send_message_text(chat_id, '---------------- ')
        except:
            send_message_text(chat_id, "Что-то сломалось")

#Жанры
    if text == 'fantasy':
        books = get_inf_book('fantasy',10)
        msg = "Книги по жанру «Фантастика»:\n"
        for i, book in enumerate(books, start=1):#enumerate - итератор который выдаёт кортежи
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):#isinstance - проверяет что authors это список list
                authors = ", ".join(authors)#склеивает список через запятую
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'horror':
        books = get_inf_book('horror', 10)
        msg = "Книги по жанру «Ужасы»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'humor':
        books = get_inf_book('humor', 10)
        msg = "Книги по жанру «Юмор»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'mystery_and_detective_stories':
        books = get_inf_book( 'mystery_and_detective_stories', 10)
        msg = "Книги по жанру «Мистика и детективы»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'science_fiction':
        books = get_inf_book( 'science_fiction', 10)
        msg = "Книги по жанру «Научная фантастика»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'religion':
        books = get_inf_book( 'religion', 10)
        msg = "Книги по жанру «Религия»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'literature':
        books = get_inf_book( 'literature', 10)
        msg = "Книги по жанру «Классика»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'psychology':
        books = get_inf_book( 'psychology', 10)
        msg = "Книги по жанру «Психология»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'programming':
        books = get_inf_book( 'programming', 10)
        msg = "Книги по жанру «Программирование»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

    if text == 'kittens':
        books = get_inf_book( 'kittens', 10)
        msg = "Книги по жанру «Котята»:\n"
        for i, book in enumerate(books, start=1):
            title = book.get('title') or 'Без названия'
            authors = book.get('author_name') or []
            if isinstance(authors, list):
                authors = ", ".join(authors)
            msg += f"{i}. {title} — {authors}\n"
        send_message_text(chat_id, msg)

