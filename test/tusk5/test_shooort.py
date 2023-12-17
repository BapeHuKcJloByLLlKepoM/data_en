import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def app_url():
    return "https://dataen-mvfulkp9imtqm24v4zhmpy.streamlit.app/"

def test_translation(driver, app_url):
    driver.get(app_url)
    try:
        text_input = driver.find_element(By.XPATH, "some example text in the English language")
        # text_input = driver.find_element(By.XPATH, '//input[@type="text"]')
        #text_input.send_keys("some example text in the English language" + Keys.ENTER)
        driver.implicitly_wait(1000)
    except NoSuchElementException:
        assert False, "Text input element not found"

    try:
        audio_element = driver.find_element(By.XPATH, '//audio')
        assert audio_element.is_displayed()
    except NoSuchElementException:
        assert False, "Audio element not found"
