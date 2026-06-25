from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def add_first_product(self):
        self.driver.find_element(By.CSS_SELECTOR, ".productcart").click()

    def open_cart(self):
        self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

    def update_quantity(self, qty):
        qty_field = self.driver.find_element(
            By.CSS_SELECTOR,
            "input[name*='quantity']"
        )

        qty_field.clear()
        qty_field.send_keys(str(qty))

        self.driver.refresh()

    def remove_product(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            "a.btn.btn-sm"
        ).click()