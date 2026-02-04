from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    REQUIRED_FIELD_ERRORS = (By.CSS_SELECTOR, ".oxd-input-group__message")

class DashboardPageLocators:
    HEADER_TEXT = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")