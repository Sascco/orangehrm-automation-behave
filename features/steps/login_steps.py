from behave import given, when, then, use_step_matcher
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

use_step_matcher("parse")


@given('the user is on the Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('the user attempts to log in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then('the system should display "{result}"')
def step_impl(context, result):
    assert context.login_page.validate_login_result(result, context.driver), \
        f'Expected "{result}" but validation failed.'