import time
import requests
import schedule

from data.data import *
from utils.utils import *
from settings.setings import url

print(get_id_admin())

def main():
    last_update_id = 0

    schedule.every().day.at(get_json_data("StartTime")).do(send_to_all_from_csv)
    schedule.every().day.at(get_json_data("EndTime")).do(send_admin_txt)
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