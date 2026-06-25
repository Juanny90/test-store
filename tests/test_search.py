from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_search_product(driver):

    home = HomePage(driver)

    home.open()
    home.search_product("shampoo")

    search = SearchPage(driver)

    assert search.page_contains("shampoo")