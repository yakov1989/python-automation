import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


# yield allows to run the test and to return to the function
@pytest.fixture()
def browser():
    options = Options()
    Options.add_argument("--headless")
    driver = webdriver.chrome(options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    # allows Selenium to wait for the page to load to search for certain element
    driver.implicitly_wait(5)
    yield driver
    print("after test")
    sleep(3)
