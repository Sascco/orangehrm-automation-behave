from src.pages.base_page import BasePage
from src.utils.locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        self.type_text(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)