class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def page_contains(self, text):
        return text.lower() in self.driver.page_source.lower()