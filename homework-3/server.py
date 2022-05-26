import flask
import time
from datetime import datetime
from flask import Flask, abort

message = {
    'name': 'Anton',
    'time': 12343,
    'text': 'text01923897'
}

app = Flask(__name__)
db = []

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def print_status():
    users = []
    for message in db:
        if message['name'] not in users:
            users.append(message['name'])
    statusnow = {
        'Текущее время': datetime.now().strftime("%H:%M:%S"),
        'Кол-во пользователей': users,
        'Кол-во пользователей в чате': len(users),
        'Кол-во сообщений': len(db),
    }

    return json.dumps(statusnow)


@app.route("/send", methods= ['POST'])
def send_messages():
    '''
    функция для отправки сообщения пользователя
    :return:
    '''
    data = flask.request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    if len(data) != 2:
        return abort(400)

    if not isinstance(data['name'], str) or \
        not isinstance(data['text'], str) or \
        len(data['name']) == 0 or \
        len(data['text']) == 0:
        return abort(400)

    text = data['text']
    name = data['name']
    message = {
        'name': name,
        'text': text,
        'time': time.time(),
    }
    db.append(message)
    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        return abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}


app.run()