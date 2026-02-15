from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.core.config import get_orange_url


class LoginPage(BasePage):
    # Locators
    _username_field = (By.NAME, "username")
    _password_field = (By.NAME, "password")
    _login_button = (By.CSS_SELECTOR, "button[type='submit']")
    _error_message = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(get_orange_url())

    def enter_username(self, username):
        self.type(self._username_field, username)

    def enter_password(self, password):
        self.type(self._password_field, password)

    def click_login(self):
        self.click(self._login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self._error_message)
    
    def validate_login_result(self, result, driver):
        if result == "Dashboard":
            from src.pages.dashboard_page import DashboardPage
            return DashboardPage(driver).is_displayed()

        elif result == "Invalid credentials":
            return "Invalid credentials" in self.get_error_message()

        elif result == "Required fields":
            return self.required_fields_displayed()

        return False