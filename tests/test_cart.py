from pages.home_page import HomePage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):

    home = HomePage(driver)
    home.open()
    home.search_product("shampoo")

    cart = CartPage(driver)
    cart.add_first_product()

    driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

    assert "Shopping Cart" in driver.page_source


def test_update_quantity(driver):

    home = HomePage(driver)

    home.open()
    home.search_product("shampoo")

    cart = CartPage(driver)

    cart.add_first_product()
    cart.add_first_product()
    driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

    assert "Shopping Cart" in driver.page_source
    cart.open_cart()
    cart.update_quantity(2)

    assert "2" in driver.page_source


def test_remove_product(driver):

    home = HomePage(driver)

    home.open()
    home.search_product("shampoo")

    cart = CartPage(driver)

    cart.add_first_product()
    driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

    assert "Shopping Cart" in driver.page_source
    cart.open_cart()
    cart.remove_product()

    assert "empty" in driver.page_source.lower()