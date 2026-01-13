from selenium.webdriver.common.by import By
from utils.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_login_page(self):
        self.driver.get(LoginPageLocators.url_orangehrm)

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.NAME, LoginPageLocators.username)))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, LoginPageLocators.password)))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, LoginPageLocators.login_button)))
        login_button.click()