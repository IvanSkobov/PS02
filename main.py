import requests
from pprint import pprint

# Задание 1: Получение данных
print("Задание 1: Получение данных")
url_1 = "https://api.github.com/search/repositories"
params_1 = {"q": "html"}
response_1 = requests.get(url_1, params=params_1)
print("Статус-код:", response_1.status_code)
print("JSON-ответ:")
pprint(response_1.json())  # Красивый вывод JSON

# Задание 2: Параметры запроса
print("\nЗадание 2: Параметры запроса")
url_2 = "https://jsonplaceholder.typicode.com/posts"
params_2 = {"userId": 1}
response_2 = requests.get(url_2, params=params_2)
print("Полученные записи:")
pprint(response_2.json())  # Красивый вывод списка записей

# Задание 3: Отправка данных
print("\nЗадание 3: Отправка данных")
url_3 = "https://jsonplaceholder.typicode.com/posts"
data_3 = {'title': 'foo', 'body': 'bar', 'userId': 1}
response_3 = requests.post(url_3, json=data_3)
print("Статус-код:", response_3.status_code)
print("Ответ:")
pprint(response_3.json())  # Красивый вывод ответа на POST-запрос
