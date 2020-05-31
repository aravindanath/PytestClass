
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield
    driver.quit()


@pytest.mark.run
def test_logina(setup):

    driver.get("https://www.google.com")
    #  actual == excepted
    pgTile = driver.title
    assert pgTile == "Google"
    search = driver.find_element_by_name("q")
    print("Search box", search.is_displayed())
    assert search.is_displayed()


@pytest.mark.run
def test_loginb(setup):
    driver.get("https://www.facebook.com/")
    fm =driver.find_element_by_id("u_0_6")
    fm.click()
    assert fm.is_selected() == True







    
# @pytest.mark.run(order=3)
# def test_two():
#     assert False
