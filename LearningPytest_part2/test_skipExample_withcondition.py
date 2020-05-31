from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

a=100

@pytest.mark.skipif(a<10,reason="Test skipping")
def test_login1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    print(driver.title)

def test_caseb():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com")
    print(driver.title)