import requests
import time

root_url = "https://api.telegram.org/bot"

ok_codes = 200, 201, 202, 203, 204

class Bot:
    
    def __init__(self,bot_token):
        self.token = bot_token

print(Bot("6009221353:AAE-011e3mATjg60zKh7t6cUXrDTeTO-G40").token)
print(Bot("Egor").token)
print(Bot("Nadzia").token)
print(Bot("Nikita").token)

# sentences = [
#     {"text": "When my time comes \n Forget the wrong that I’ve done take.",
#      "level": 1},
#     {"text": "In a hole in the ground there lived a hobbit.",
#      "level": 2},
#     {"text": "The sky the port was the color of television, tuned to a dead channel take.",
#      "level": 1},
#     {"text": "I love the smell of napalm in the morning.",
#      "level": 0},
#     {"text": "The man in black fled across the desert, and the gunslinger followed.",
#      "level": 0},
#     {"text": "The Consul watched as Kassad raised the death wand.",
#      "level": 1},
#     {"text": "If you want to make enemies, try to change something.",
#      "level": 2},
#     {"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
#      "level": 1},
#     {"text": "I learned very early the difference between knowing the name of something and knowing something.",
#      "level": 2}
# ]


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



# def get_updates(token):
# 	url = f"{root_url}{token}/getUpdates"
# 	res = requests.get(url)
# 	if res.status_code in ok_codes:
# 		updates = res.json()
# 		return updates


# def send_message(text, chat_id, token):
# 	url = f"{root_url}{token}/sendMessage"
# 	res = requests.post(url, data = {'chat_id': chat_id, 'text': sens})
# 	if res.status_code in ok_codes:
# 		return True
# 	else:
# 		return False	

# last_message_id = 0

# while True:
# 	time.sleep(2)
# 	Updates = get_updates(token)
# 	if len(Updates["result"]) > 0:
# 		last_message = Updates["result"][-1]
# 		last_message_text = last_message["message"]["text"]
# 		chat_id = last_message["message"]["chat"]["id"]
# 		message_id = Updates["result"][-1]["message"]["message_id"]
# 		if message_id > last_message_id:
# 			send_message(last_message_text, chat_id, token)
# 			last_message_id = message_id
# 	else:
# 		print("no message")    	