import requests

API_URL = "http://35.237.179.38:8501"
ENDPOINT = "/synthesize_tts"

def test_synthesize_tts():
    # Test case 1: Check if the API is up and running
    response = requests.get(API_URL + "/healthcheck")
    assert response.status_code == 200

    # Test case 2: Send a POST request to synthesize TTS
    payload = {
        "text": "Hello, world!",
        "voice": "en-US"
    }
    response = requests.post(API_URL + ENDPOINT, json=payload)
    assert response.status_code == 200

    # Test case 3: Check the response content
    data = response.json()
    assert "audio" in data
    assert isinstance(data["audio"], str)

if __name__ == "__main__":
    test_synthesize_tts()
