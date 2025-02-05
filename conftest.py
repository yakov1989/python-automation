import pytest
from selenium import webdriver
from time import sleep


# yield allows to run the test and to return to the function
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # allows Selenium to wait for the page to load to search for certain element
    driver.implicitly_wait(5)
    yield driver
    print("after test")
    sleep(3)
