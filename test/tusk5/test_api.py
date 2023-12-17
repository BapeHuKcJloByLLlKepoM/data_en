import requests

API_URL = "https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app/"
ENDPOINT = "/synthesize_tts"

def test_synthesize_tts():
    # Тест 1: проверка работоспособности API
    response = requests.get(API_URL + "/healthcheck")
    assert response.status_code == 200

    # Тест 2: Запрос на озвучивание текста
    payload = {
        "text": "Hello, world!",
        "voice": "en-US"
    }
    response = requests.post(API_URL + ENDPOINT, json=payload)
    assert response.status_code == 200

    # Тест 3: Проверьте содержимое ответа
    data = response.json()
    assert "audio" in data
    assert isinstance(data["audio"], str)

if __name__ == "__main__":
    test_synthesize_tts()
