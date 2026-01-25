import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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
    # Find the number '2' button by ID
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2").click()
    
    # Find the '+' button (Accessibility ID is often better/stable)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "plus").click()
    
    # Click '2' again
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2").click()
    
    # Click '='
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
    
    # 3. VERIFY: Check result
    result_element = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final")
    result_text = result_element.text
    
    print(f"Result is: {result_text}")
    assert result_text == "4"


    # 2. TEST: Do 2 * 2 = 4
def test_multiplication(driver):
    # Find the number '2' button by ID
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2").click()
    
    # Find the '+' button (Accessibility ID is often better/stable)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "multiply").click()
    
    # Click '2' again
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2").click()
    
    # Click '='
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
    
    # 3. VERIFY: Check result
    result_element = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final")
    result_text = result_element.text
    
    print(f"Result is: {result_text}")
    assert result_text == "4"

    