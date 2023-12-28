# import unittest
# import requests

# class TestMMS_TTS_EngAPI(unittest.TestCase):
#     def test_text_to_speech(self):
#         url = "https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app"
#         data = {
#             "text": "Hello, world!",
#             "voice": "default"
#         }
        
#         response = requests.post(url, json=data)
#         response_data = response.json()
        
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("audio_url", response_data)
#         self.assertIn("metadata", response_data)
#         self.assertEqual(response_data["metadata"]["language"], "en")
    
#     def test_supported_voices(self):
#         url = "https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app"
        
#         response = requests.get(url)
#         response_data = response.json()
        
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response_data, list)
#         self.assertGreater(len(response_data), 0)
#         self.assertIn("default", response_data)  # Проверяем, что 'default' голос доступен
    
#     def test_health_check(self):
#         url = "https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app"
        
#         response = requests.get(url)
        
#         self.assertEqual(response.status_code, 200)

# if __name__ == "__main__":
#     unittest.main()
