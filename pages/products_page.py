from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, browser):
        self.browser = browser

    def validate_product_page_title(self, expected_title="Products"):
        # Search using XPATH
        products_page_title = self.browser.find_element(By.XPATH, value='//*[@data-test="title"]').text
        print(f"{products_page_title = }")
        assert products_page_title == "Products"

    def validate_products_page_url(self):
        current_url = self.browser.current_url
        print(f"{current_url=}")
        assert current_url == "https://www.saucedemo.com/inventory.html"
