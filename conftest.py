import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


# yield allows to run the test and to return to the function
@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless")  # the browser operates without opening a graphical user interface (GUI)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # allows Selenium to wait for the page to load to search for certain element
    driver.implicitly_wait(5)
    yield driver
    sleep(3)
