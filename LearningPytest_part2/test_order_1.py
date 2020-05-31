
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.run(order =2)
def test_logina():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    assert driver.title == "Google"

@pytest.mark.run(order = 1)
def test_loginb():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com")
    emailText = driver.find_element_by_id("email")
    assert emailText.is_displayed()
    assert driver.title == driver.title
    assert driver.current_url == "https://www.facebook.com"


    
# @pytest.mark.run(order=3)
# def test_two():
#     assert False
