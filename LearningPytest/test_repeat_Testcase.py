from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.repeat(2)
def test_login1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    print(driver.title)

@pytest.mark.repeat(2)
def test_caseb():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com")
    print(driver.title)