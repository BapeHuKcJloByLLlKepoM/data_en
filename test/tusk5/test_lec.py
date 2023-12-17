import pytest
import requests
import streamlit as st


def test_app_running():
    response = requests.get("https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app/")
    assert response.status_code == 200


def test_text_to_speech_translation():
    text = "Hello"
    response = requests.post("https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app/",
                             data={"text": text})
    assert response.status_code == 200
    assert "streamlit-audio-element" in response.text
    assert "audio/wav" in response.headers["Content-Type"]


@pytest.fixture(scope="session", autouse=True)
def run_streamlit_app():
    st._is_running_with_streamlit = True
    import tusk2_4_5.streamlit_app  # Replace "app" with the filename of your Streamlit app
    yield


if __name__ == "__main__":
    pytest.main([__file__])
