import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from util import ActionHelpers  # <--- IMPORT THE HELPER

# 1. SETUP: Connect to the Phone
@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    
    # This tells Appium to open the Google Calculator
    options.set_capability("appPackage", "com.google.android.calculator")
    options.set_capability("appActivity", "com.android.calculator2.Calculator")

    # Connect to local Appium server
    # Make sure you have 'appium' running in a separate terminal!
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # Implicit wait helps avoid "Element not found" if the app is slow to load
    driver.implicitly_wait(10)
    
    yield driver
    
    # TEARDOWN: Close the app
    driver.quit()

# 2. TEST: Do 2 + 2 = 4
def test_addition(driver):
    
    # Initialize the Helper with the current driver
    actions = ActionHelpers(driver)

    # Find the number '2' button by ID
    actions.wait_and_click(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    
    # Find the '+' button (Accessibility ID is often better/stable)
    actions.wait_and_click(AppiumBy.ACCESSIBILITY_ID, "plus")
    
    # Click '2' again
    actions.wait_and_click(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    
    # Click '='
    actions.wait_and_click(AppiumBy.ACCESSIBILITY_ID, "equals")
    
    # 3. VERIFY: Check result
    result_text = actions.wait_and_get_text(AppiumBy.ID, "com.google.android.calculator:id/result_final")    
    
    print(f"Result is: {result_text}")
    assert result_text == "4"


    # 2. TEST: Do 2 * 2 = 4
def test_multiplication(driver):
    # Initialize the Helper with the current driver
    actions = ActionHelpers(driver)

    # Find the number '2' button by ID
    actions.wait_and_click(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    
    # Find the '+' button (Accessibility ID is often better/stable)
    actions.wait_and_click(AppiumBy.ACCESSIBILITY_ID, "multiply")
    
    # Click '2' again
    actions.wait_and_click(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    
    # Click '='
    actions.wait_and_click(AppiumBy.ACCESSIBILITY_ID, "equals")
    
    # 3. VERIFY: Check result
    result_text = actions.wait_and_get_text(AppiumBy.ID, "com.google.android.calculator:id/result_final")    
    
    print(f"Result is: {result_text}")
    assert result_text == "4"

    