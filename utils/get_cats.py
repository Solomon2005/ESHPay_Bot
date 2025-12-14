import requests
import json
import time
import random

from settings.setings import url_cat, url_bot

url = f'https://api.telegram.org/bot{url_bot}/sendPhoto'

def get_img_cat(chat_id):
    try:
        ts = int(time.time())
        response = requests.get(url_cat)
        params = {
            "chat_id":chat_id,
        }
        data={
            "photo": f"{url_cat}?t={ts}"
        }

        mes_resp = requests.post(url, params=params, data=data)

    except:
        num = random.randint(1, 5)
        with open(f"utils/cats/{num}.jpg", mode='rb') as f:
            img = f.read()

            cat_content = img

            params={
                'chat_id':chat_id,
            }
            data={
                'photo': cat_content
            }

            mes_resp = requests.post(url, params=params, files=data)
