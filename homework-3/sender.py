import requests

anonymous = input('Для анонимных сообщений написать "+": ')
if anonymous == "+":
    name = 'Анонимный пользователь'
else:
  name = input('Введите имя: ')

while True:
    text = input('Введите sms: ')
    response = requests.post('http://127.0.0.1:5000/send',
                             json={
                                 'name': name,
                                 'text': text
                             }
                            )