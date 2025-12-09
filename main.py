import time

from Data.Data import *
from body.batton import updates
from settings.setings import *
from body import *


def main():
    last_update_id = 0
    while True:
        try:
            updates = requests.get(f'{url}getUpdates', params={'offset': last_update_id, 'timeout': 10}).json()
            for update in updates:
                last_update_id = update['update_id']+1
                if 'message' in update:
                    pass
                if 'location' in update:
                    pass
                if 'photo' in update:
                    pass
                elif 'callback_query' in update:
                    pass
        except:
            time.sleep(3)


if __name__ == '__main__':
    chack_Notes_csv()
    main()
