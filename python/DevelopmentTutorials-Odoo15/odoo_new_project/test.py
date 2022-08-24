 
 
import json
import requests
url = 'https://api.weatherapi.com/v1/current.json?key=ea5cec8b4a60443684f83726220808&q=hanoi'
data = requests.get(url)
data = data.json()
with open('test.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False))