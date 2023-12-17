import requests

url = "https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app/"
timeout = 5  # Установите желаемое значение таймаута в секундах

try:
    response = requests.get(url, timeout=timeout)
    # Далее обрабатывайте ответ сервера...
except requests.exceptions.Timeout:
    print("Таймаут запроса. Проверьте подключение к серверу.")
except requests.exceptions.RequestException as e:
    print("Ошибка во время запроса:", e)
