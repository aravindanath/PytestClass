
from selenium.webdriver import Chrome
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def setPath():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield
    driver.close()

# @pytest.mark.Hello
def test_case_f(setPath):

    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    
# @pytest.mark.Hi 
def test_case_g(setPath):

    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
#     assert driver.current_url == "https://www.facebook.com/"
    
    
    
# @pytest.mark.Hello 
def test_h(setPath):

    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()