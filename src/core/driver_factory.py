from encodings.punycode import T

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome", headless=True):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")

        if headless:
            options.add_argument("--headless")

        if browser.lower() == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(10)
    
        return driver