from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://automationteststore.com/")

    def click_login(self):
        self.driver.find_element(
            By.LINK_TEXT,
            "Login or register"
        ).click()

    def search_product(self, product):
        search = self.driver.find_element(
            By.ID,
            "filter_keyword"
        )

        search.clear()
        search.send_keys(product)

        self.driver.find_element(
            By.CSS_SELECTOR,
            ".button-in-search"
        ).click()