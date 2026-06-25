from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_success(driver):

    home = HomePage(driver)
    home.open()
    home.click_login()

    login = LoginPage(driver)

    login.login(
        "usuario_valido",
        "password_valida"
    )

    assert "login" in driver.current_url.lower()

def test_login_invalid(driver):

    home = HomePage(driver)
    home.open()
    home.click_login()

    login = LoginPage(driver)

    login.login(
        "usuario_falso",
        "password_falsa"
    )

    assert "Error" in driver.page_source