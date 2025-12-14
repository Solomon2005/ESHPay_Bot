import time, datetime
import requests
import schedule

from Data.Data import *
from utils.utils import *
from settings.setings import url


def main():
    last_update_id = 0

    schedule.every().day.at("08:00").do(send_to_all_from_csv)
    schedule.every().day.at("23:55").do(send_admin_txt)
    while True:
        try:
            response = requests.get(f'{url}getUpdates', params={'offset': last_update_id, 'timeout': 10}).json()
            get_chak_mess(response)
            get_RESULT_txt(response)
            for update in response['result']:
                last_update_id = update['update_id']+1
                if 'message' in update:
                    messages(update['message'])
                elif 'callback_query' in update:
                    buttom_message(update['callback_query'])

            schedule.run_pending()
            time.sleep(1)
        except:
            print("Something went wrong")
            time.sleep(3)


if __name__ == '__main__':
    chack_Start_csv()
    chack_Notes_csv()
    chack_RESULT_txt()
    main()