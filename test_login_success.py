from src.core.driver_factory import DriverFactory
from src.core.config import get_orange_url, get_orange_username, get_orange_password
from src.pages.login_page import LoginPage

def test_login_correcto():
    driver = DriverFactory.get_driver()
    driver.get(get_orange_url())

    login_page = LoginPage(driver)
    login_page.login(get_orange_username(), get_orange_password())

    # Aquí luego validaremos que llegamos al dashboard

    driver.quit()