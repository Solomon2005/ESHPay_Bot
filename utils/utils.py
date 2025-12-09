import requests
import json
from settings.setings import url_bot

url = url_bot

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

def get_chak_mess():
    update_response = requests.get(f'{url}{"getUpdates"}').json()
    print(json.dumps(update_response, indent=4,  ensure_ascii=False))