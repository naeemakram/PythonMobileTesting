# utils.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ActionHelpers:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, by_locator, value, timeout=10):
        """
        Retries finding the element for 'timeout' seconds. 
        If found, clicks it.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((by_locator, value)))
            element.click()
        except TimeoutException:
            print(f"🚨 Error: Could not find clickable element '{value}' after {timeout} seconds.")
            raise

    def wait_and_get_text(self, by_locator, value, timeout=10):
        """
        Waits for element to be present and returns its text.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((by_locator, value)))
            return element.text
        except TimeoutException:
            print(f"🚨 Error: Could not find element '{value}' to read text.")
            raise