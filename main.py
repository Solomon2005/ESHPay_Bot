import time

from Data.Data import *
from body.batton import *
from settings.setings import *
from body import *
from utils.utils import *


def main():
    last_update_id = 0
    while True:
        try:
            response = requests.get(f'{url}getUpdates', params={'offset': last_update_id, 'timeout': 10}).json()
            for update in response['result']:
                last_update_id = update['update_id']+1
                if 'message' in update:
                    messages(update['message'])
                if 'location' in update:
                    pass
                if 'photo' in update:
                    pass
                elif 'callback_query' in update:
                    buttom_message(update['callback_query'])
        except:
            time.sleep(3)


if __name__ == '__main__':
    chack_Notes_csv()
    main()
