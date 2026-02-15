from src.core.driver_factory import DriverFactory
from src.pages.login_page import LoginPage
from src.core.config import get_orange_url

def before_scenario(context, scenario):

    context.driver = DriverFactory.get_driver()
    context.driver.get(get_orange_url())
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):

    if hasattr(context, 'driver'):
        context.driver.quit()

def after_step(context, step):

    if step.status == "failed":
        # We will implement screenshot logic here in Phase 2
        pass