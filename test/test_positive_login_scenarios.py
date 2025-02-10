from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


# yield allows to run the test and to return to the function


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
