from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CalculatorPage(BasePage):
    # 1. LOCATORS (The "Map")
    # Store them here so if IDs change, you only edit this section.
    DIGIT_2 = (AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    DIGIT_4 = (AppiumBy.ID, "com.google.android.calculator:id/digit_4")
    PLUS_BTN = (AppiumBy.ACCESSIBILITY_ID, "plus")
    MULTIPLY_BTN = (AppiumBy.ACCESSIBILITY_ID, "multiply")
    SUBTRACT_BTN = (AppiumBy.ACCESSIBILITY_ID, "minus")
    EQUALS_BTN = (AppiumBy.ACCESSIBILITY_ID, "equals")
    RESULT_SCREEN = (AppiumBy.ID, "com.google.android.calculator:id/result_final")

    # 2. ACTIONS (The "Behaviors")
    def tap_two(self):
        self.click(self.DIGIT_2)
    
    def tap_four(self):
        self.click(self.DIGIT_4)

    def tap_plus(self):
        self.click(self.PLUS_BTN)        

    def tap_multiply(self):
        self.click(self.MULTIPLY_BTN)

    def tap_subtract(self):
        self.click(self.SUBTRACT_BTN)

    def tap_equals(self):
        self.click(self.EQUALS_BTN)

    def get_result(self):
        return self.get_text(self.RESULT_SCREEN)

    # 3. WORKFLOWS (Optional: Combine steps)
    def calculate_two_plus_two(self):
        self.tap_two()
        self.tap_plus()
        self.tap_two()
        self.tap_equals()

    def calculate_two_multiply_two(self):
        self.tap_two()
        self.tap_multiply()
        self.tap_two()
        self.tap_equals()


    def calculate_four_minus_two(self):
        self.tap_four()
        self.tap_subtract()
        self.tap_two()
        self.tap_equals()