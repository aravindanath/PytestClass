from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


# Decorator
@pytest.mark.skip(reason="Learning test skipping")
def test_login1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    print(driver.title)

def test_caseb():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com")
    print(driver.title)