import unittest
import requests

class TestMmsTtsAPI(unittest.TestCase):
    def test_synthesize_text(self):
        text = "Hello, how are you?"
        response = requests.post("https://appapppy-glg9ykmarcwvxrb4agbxyd.streamlit.app/synthesize_text", json={"text": text})

        # Проверяем статус код ответа
        self.assertEqual(response.status_code, 200)
        
        # Проверяем, что поле 'audio' присутствует в ответе
        self.assertIn('audio', response.json())
        
        # Проверяем, что поле 'audio' не пустое
        self.assertNotEqual(response.json()['audio'], '')

if __name__ == '__main__':
    unittest.main()
