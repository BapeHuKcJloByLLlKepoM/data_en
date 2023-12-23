import requests

url = "http://34.125.57.194:8501"
timeout = 1000  # Установите желаемое значение таймаута в секундах

try:
    response = requests.get(url, timeout=timeout)
    # Далее обрабатывайте ответ сервера...
except requests.exceptions.Timeout:
    print("Таймаут запроса. Проверьте подключение к серверу.")
except requests.exceptions.RequestException as e:
    print("Ошибка во время запроса:", e)
