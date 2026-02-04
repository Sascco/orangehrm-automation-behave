# En test_driver.py
from src.core.driver_factory import DriverFactory

driver = DriverFactory.get_driver()
driver.get("https://opensource-demo.orangehrmlive.com/")
input("Presiona Enter para cerrar el navegador...")
driver.quit()