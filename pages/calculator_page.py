from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CalculatorPage(BasePage):
    # 1. LOCATORS (The "Map")
    # Store them here so if IDs change, you only edit this section.
    PLUS_BTN = (AppiumBy.ACCESSIBILITY_ID, "plus")
    MULTIPLY_BTN = (AppiumBy.ACCESSIBILITY_ID, "multiply")
    SUBTRACT_BTN = (AppiumBy.ACCESSIBILITY_ID, "minus")
    DIVIDE_BTN = (AppiumBy.ACCESSIBILITY_ID, "divide")
    EQUALS_BTN = (AppiumBy.ACCESSIBILITY_ID, "equals")
    RESULT_SCREEN = (AppiumBy.ID, "com.google.android.calculator:id/result_final")

    def tap_plus(self):
        self.click(self.PLUS_BTN)        

    def tap_multiply(self):
        self.click(self.MULTIPLY_BTN)

    def tap_subtract(self):
        self.click(self.SUBTRACT_BTN)

    def tap_divide(self):
        self.click(self.DIVIDE_BTN)

    def tap_equals(self):
        self.click(self.EQUALS_BTN)

    def get_result(self):
        return self.get_text(self.RESULT_SCREEN)

