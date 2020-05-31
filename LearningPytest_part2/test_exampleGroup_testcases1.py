

import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def setPath():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield
    driver.close()

@pytest.mark.Hello
def test_case_a(setPath):
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    
@pytest.mark.Hi
def test_case_b(setPath):
    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    assert driver.current_url == "https://www.facebook.com/"
    
    
    
@pytest.mark.Hello
def test_c(setPath):

    driver.get("https://www.amazon.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()