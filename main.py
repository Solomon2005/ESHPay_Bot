import time
import requests

from Data.Data import chack_Notes_csv
from utils.utils import get_chak_mess, messages, buttom_message
from settings.setings import url


def main():
    last_update_id = 0
    while True:
        time.sleep(3)
        try:
            response = requests.get(f'{url}getUpdates', params={'offset': last_update_id, 'timeout': 10}).json()
            get_chak_mess(response)
            for update in response['result']:
                last_update_id = update['update_id']+1
                if 'message' in update:
                    messages(update['message'])
                elif 'callback_query' in update:
                    buttom_message(update['callback_query'])
        except:
            time.sleep(3)


if __name__ == '__main__':
    chack_Notes_csv()
    main()
