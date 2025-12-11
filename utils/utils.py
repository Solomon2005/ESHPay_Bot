import requests
import json

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
            send_message_text(chat_id,'работает1')
            add_new_notes(message)
            send_message_text(chat_id, 'Заметка сохранена')

        if 'Заметки:' in text:
            send_message_text(chat_id, 'Напиши "Заметка" в место "Заметки"')
    if 'photo' in message:
        send_message_text(chat_id,"нахуй мне твоё фото")
    if 'document' in message:
        send_message_text(chat_id,"Засунь себе свой документ")

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