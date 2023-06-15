import requests
import time
from settings import root_url, ok_codes

class Bot:
    def __init__(self, bot_token):
        self.token = bot_token

    def get_updates(self):
        url = f"{root_url}{self.token}/getUpdates"
        res = requests.get(url)
        if res.status_code in ok_codes:
            updates = res.json()
            return updates

    def send_message(self, text, chat_id):
        url = f"{root_url}{self.token}/sendMessage"
        res = requests.post(url, data = {'chat_id': chat_id, 'text': text})
        if res.status_code in ok_codes:
            return True
        else:
            return False    


    def polling(self):
        last_message_id = 0
        while True:
            time.sleep(2)
            updates = self.get_updates()
            if len(updates["result"]) > 0:
                last_message = updates["result"][-1]
                last_message_text = last_message["message"]["text"]
                chat_id = last_message["message"]["chat"]["id"]
                message_id = updates["result"][-1]["message"]["message_id"]
                if message_id > last_message_id:
                    self.send_message(last_message_text, chat_id)
                    last_message_id = message_id


# def search_text(sentences, last_message_text):
#     result_list = []
#     result_message = ""

#     for sentence in sentences:
#         if last_message_text.get("text") in sentence.get("text"):
#             result_list.append(sentence.get("text"))

#     if len(result_list) == 0:
#         result_message = "Does not exist"
#     if len(result_list) == 1:
#         result_message = result_list[0]

#     if len(result_list) > 1:
#         for result in result_list:
#             result_message = result_message + "\n **** \n" + result
#     return result_list