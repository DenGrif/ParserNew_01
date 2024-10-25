import requests

# URL API для запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки в виде словаря
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса с данными
response = requests.post(url, json=data)

# Распечатка статус-кода ответа
print("Статус-код:", response.status_code)

# Распечатка содержимого ответа
print("Содержимое ответа:", response.json())