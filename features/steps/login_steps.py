from behave import given, when, then
from src.pages.login_page import LoginPage
from selenium import webdriver


@given('que estoy en la página de Login')
def step_impl(context):
    # El driver ya se abre en environment.py, aquí solo validamos que cargó
    context.login_page = LoginPage(context.driver)

@when('el usuario ingresa el nombre de usuario "{user}"')
def step_impl(context, user):
    context.login_page.enter_username(user)

@when('el usuario ingresa la contraseña "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('el usuario hace clic en el botón "Login"')
def step_impl(context):
    context.login_page.click_login()

@then('el sistema debe redirigirlo a la página de "Dashboard"')
def step_impl(context):
    # Validamos que la URL contenga 'dashboard'
    assert "dashboard" in context.driver.current_url.lower()

@then('el encabezado de la página debe mostrar el texto "Dashboard"')
def step_impl(context):
    from src.utils.locators import DashboardPageLocators
    header = context.driver.find_element(*DashboardPageLocators.HEADER_TEXT).text
    assert header == "Dashboard"