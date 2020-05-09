from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import os
from flask_sslify import SSLify
app = Flask(__name__)
sslify = SSLify(app)
KEY = os.getenv('API_KEY')
URL = 'https://api.telegram.org/bot' + KEY

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def send_message(chat_id, text='!'):
    url = URL + '/sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        if 'Привет' in message:
            send_message(chat_id, text='Hi!')

        return jsonify(r)
    return '<h1>webpage</h1>'

if __name__ == '__main__':
    app.run()
