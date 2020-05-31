
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging
import sys
import allure
from allure_commons.types import AttachmentType


logger=logging.getLogger()
logger.setLevel(logging.INFO)





@pytest.fixture(scope='module')
def setPath():
    global driver
    driver =Chrome(ChromeDriverManager().install())
    yield
    driver.close()

# @pytest.mark.Hello
def test_case_a(setPath):
    with allure.step("Facebook Home Screenshot!!"): 
        driver.get("https://www.facebook.com/")
        driver.find_element_by_id("email").send_keys("its23@gmail.com")
        driver.find_element_by_xpath("//*[@id='u_0_2']").click()
        allure.attach(driver.get_screenshot_as_png(), "Screenshot of the screen" ,AttachmentType.PNG)
        driver.implicitly_wait(5)
        driver.maximize_window()
        logger.info("Logged info message")
        logger.critical("critical level")
        logger.error("Error occured")
        print("Message outout stdout")
        print("Message output stderr ", file=sys.stderr)
        assert False
    
