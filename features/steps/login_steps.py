from behave import given, when, then
from src.core.driver_factory import DriverFactory
from src.pages.login_page import LoginPage
from src.core.config import get_orange_url

@given('I am on the Login page')
def step_impl(context):
    context.driver = DriverFactory.get_driver()
    context.driver.get(get_orange_url())
    context.login_page = LoginPage(context.driver)

@when('the user enters the username "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('the user enters the password "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('the user clicks on the "{button_name}" button')
def step_impl(context, button_name):
    context.login_page.click_login()

@then('the system should redirect to the "{page_name}" page')
def step_impl(context, page_name):
    assert page_name.lower() in context.driver.current_url.lower(), \
        f"Expected to be on {page_name} page but current URL is {context.driver.current_url}"

@then('the system should display an error message "{error_message}"')
def step_impl(context, error_message):
    actual_error = context.login_page.get_error_message()
    assert actual_error == error_message, \
        f"Expected error message '{error_message}' but got '{actual_error}'"

@then('the username and password fields should remain visible')
def step_impl(context):
    # This validates that we're still on the login page
    assert "login" in context.driver.current_url.lower()