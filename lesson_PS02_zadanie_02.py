import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    'userId': 1
}

response = requests.get(url, params=params)

pprint(response.json())
