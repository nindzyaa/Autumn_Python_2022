import requests
r = requests.get('http://127.0.0.1:5000/messages'),
print(r.status_code)
data = r.json()['messages']
print(data)