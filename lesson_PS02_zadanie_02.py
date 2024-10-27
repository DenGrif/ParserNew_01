import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    'userId': 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    pprint(response.json())
else:
    print(f"Ошибка: {response.status_code}")