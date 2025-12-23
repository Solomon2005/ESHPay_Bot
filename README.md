### Название бота:  
КНИЖНЫЙ_БОТ
### Тема бота: 
Предоставление списка книг по выбранному жанру и запись Заметок
### Список авторов:
-> Усатый Семён Владимирович  
-> Синигивская Дарья Владиславовна
### usertag:
@I_notnow_bot
### Описание и функции:
--> Запуск функционала бота через файл main.py
--> Отправка сообщения всем пользователям бота в определённое время определённый текст,
текст берётся из файла text.txt, время из task.json
--> Отправка файла с отчётом работы бота определённым пользователям,
файл с именем dataRESULT.txt, id пользователей, которым отправится файл берётся из config.json, 
после отправки удаляет содержимое файла
--> Отправляет последний ответ сервера на HTTP запрос в терминал Python
--> Добавляет последний ответ сервера на HTTP в файл dataRESULT.txt
--> Проверяет на наличие файла dataSTART.csv, при его отсутствии создаёт его
--> Проверяет на наличие файла dataRESULT.txt, при его отсутствии создаёт его
--> Проверяет на наличие файла dataNotes.csv, при его отсутствии создаёт его
--> Записывает заметки в csv таблицу и выводит записанные заметки в отдельных сообщениях
--> Реагирует на разный формат сообщений
--> На формат location отправляет название приблизительной локации по широте и долготе
--> Выводит 10 книг и их автора/авторов на выбранную тему
### Библиотеки:
-> dotenv - позволяет загружать переменные окружения из файла .env
-> schedule - планировщик задач с удобным синтаксисом
-> requests - хранение информации о запросе HttpRequest
### Список API:
-> openlibrary.org
-> cataas.com
-> catalog.api.2gis.com
### Источники:
#### -> Документации:
--> https://pypi.org/project/python-dotenv/
--> https://pypi.org/project/schedule/
--> https://metanit.com/python/django/3.7.php
#### -> Помощь для создания кода:
--> https://github.com/dbader/schedule/issues/37 # когда была проблема в shedule с модулем every
--> https://metanit.com/sharp/aspnet6/2.5.php # метанит по реквесту
--> https://metanit.com/python/django/3.7.php # метанит по реквесту
--> https://metanit.com/python/tutorial/8.1.php # когда были проблемы с datatime
--> https://metanit.com/sharp/mvc/10.7.php # метанит формата JSON
--> https://metanit.com/python/tutorial/4.5.php # метанит модуля os и работы с ним
--> https://ru.stackoverflow.com/questions/1157560/%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-json-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85 # Работа с JSON, вывод определенных данных
--> https://core.telegram.org/bots/api#inlinekeyboardbutton # документация по работе с TG ботом
--> https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard2.py # брали и перерабатывали некоторые части кода
--> https://www.youtube.com/watch?v=JVQNywo4AbU # работа с API на питоне
--> https://openlibrary.org/developers/api # руководство по работе с API openlibrary
--> https://cataas.com/ # руководство по API cataas
--> https://metanit.com/python/tutorial/2.11.php # try except
--> https://docs.2gis.com/api/search/geocoder/overview # работа для api 2 гис