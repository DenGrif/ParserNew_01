import requests
import pprint

url = "https://api.github.com/search/repositories"

params = {
    'q': 'html'
}

response = requests.get(url, params=params)

print("Статус-код:", response.status_code)

pprint.pprint(response.json())
