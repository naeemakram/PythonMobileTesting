from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        """
        Generic finder with Explicit Wait.
        locator: tuple like (AppiumBy.ID, "element_id")
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """
        Waits for element to be clickable, then clicks.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text(self, locator):
        """
        Waits for element and returns text.
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
    
    # Dynamic Action: Tap ANY digit
    def tap_digit(self, digit_str):
        # We construct the ID string dynamically based on the input 'digit_str'
        # e.g., if input is "5", locator becomes "...id/digit_5"
        if not digit_str.isdigit():
            raise ValueError(f"🚨 Invalid input: '{digit_str}'. This method only accepts digits 0-9.")
        
        locator_id = f"com.google.android.calculator:id/digit_{digit_str}"
        self.click((AppiumBy.ID, locator_id))