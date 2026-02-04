import pytest
from src.core.driver_factory import DriverFactory
from src.core.config import get_orange_url, get_orange_username, get_orange_password
from src.pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    # Teardown: Execute after the test
    driver.quit()

def test_login_exitoso(driver):
    # 1. Navigate to the page
    driver.get(get_orange_url())
    
    # 2. Initialize the Login page 
    login_page = LoginPage(driver)
    
    # 3. Perform login using environment variables
    login_page.login(get_orange_username(), get_orange_password())
    
    # 4. Validation step (Assert)
    # For now we will validate that the URL changed to include "dashboard"
    assert "dashboard" in driver.current_url.lower()
    print("Successful login test completed.")