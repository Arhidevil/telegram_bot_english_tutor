from bot import Bot
from os import environ as env
from flask import Flask, jsonify, request

app = Flask(__name__)
# token = "5587140167:AAHppe3B_3JEXeiFmASuCdIyLSSj_EOHlGQ"
token = env.get("TELEGRAM_TOKEN")

@app.route('/')
def index():
    print("Hello World")
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@app.route('/process_message', methods=['POST'])
def process_message():
    bot = Bot(token)

    update = request.json

    chat_id = update["message"]["chat"]["id"]
    message_text = update["message"]["text"]
    
    bot.send_message(message_text, chat_id)

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    if not token: 
        raise Exception("TELEGRAM_TOKEN is not defined")
    app.run(host='0.0.0.0', port=8080)
