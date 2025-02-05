import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


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


def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the APP
    login_page.open_home_page()

    # Filling Form
    login_page.type_username("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    # Validation of redirection
    current_url = browser.current_url
    print(f"{current_url=}")

    assert current_url == "https://www.saucedemo.com/inventory.html"
    # Search using XPATH
    products_page_title = browser.find_element(By.XPATH, value='//*[@data-test="title"]').text
    print(f"{products_page_title = }")
    assert products_page_title == "Products"


