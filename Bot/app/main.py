from flask import Flask
from flask import request
from flask import jsonify
import requests
import os
from flask_sslify import SSLify
app = Flask(__name__)
sslify = SSLify(app)
KEY = os.getenv('API_KEY')
URL = 'https://api.telegram.org/bot' + KEY

def send_message(chat_id, text='!'): # отправляем сообщение в чат
    url = URL + '/sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

@app.route('/', methods=['POST', 'GET'])  # получение сообщений боту и подготовка текста для ответа
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        if '/help' in message:
            send_message(chat_id, text = 'Выбери /start для запуска \ud83d\udef0')
        if '/start' in message:
            send_message(chat_id, text = 'Ближайшие мероприятия на которые планируется влететь:\n24-26 июля - Present Perfect Festival\nОфициальный сайт: runited.ru/ppf/2020\nЛента организаторов в тг: t.me/rootsunited_ppf\n\n5-6 сентября 2020 - Gamma Festival\nОфициальный сайт: gammafestival.ru\nЛента организаторов в тг: t.me/m_division')
        if 'уебло' in message:
            send_message(chat_id, text = 'Полёт нормальный!\nНе очень.')
        return jsonify(r)
    return '<h1>webpage</h1>'

if __name__ == '__main__':
    app.run()
