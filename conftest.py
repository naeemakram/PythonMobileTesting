import datetime
import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path
from pytest_html import extras

@pytest.fixture(scope="function")
def driver(request):
    # 1. Desired Capabilities
    # This tells Appium what app to test and on what device.
    # You might need to change these based on your setup.
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "",  # or your device name/UDID
        "appPackage": "com.google.android.calculator",
        "appActivity": "com.android.calculator2.Calculator",
        "language": "en",
        "locale": "US"
    }

    # 2. Appium Server URL
    # Make sure your Appium server is running on this address.
    #appium_server_url = "http://localhost:4723"
    
    # 3. Initialize Driver
    # Converts capabilities to options object and creates the driver.

    options = UiAutomator2Options()
    options.platform_name = "Android"

    # 1. Device Farm Logic (Find ANY real phone)
    options.set_capability("appium:deviceType", "real")

    # 2. App Logic (Open Calculator)
    options.set_capability("appPackage", "com.google.android.calculator")
    options.set_capability("appActivity", "com.android.calculator2.Calculator")

    # 3. Connect using the Compatibility Path
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    # 4. Yield Driver to Test
    # The test runs here.
    # 👇 CRITICAL STEP: Attach driver to the test node
    # This acts as the "Bridge" allowing the Hook to find the driver
    request.node.driver = driver

    yield driver

    # 5. Teardown
    # This runs after the test is finished.
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    
    # We only look at the "call" stage (the actual test execution)
    if report.when == "call":
        # Check if test failed OR if you want it for passed tests too
        # Change to: "if True:" to capture screenshot for EVERY test
        if report.failed or report.passed: 
            
            # Get the driver from the test item
            driver = getattr(item, "driver", None)
            
            if driver:
                # 1. Capture Screenshot as Base64 (Text) instead of File
                screenshot_base64 = driver.get_screenshot_as_base64()
                
                # 2. Create an HTML <div> for the image
                # (You can just pass the base64 string, but this format is safer)
                html_image = f'<div><img src="data:image/png;base64,{screenshot_base64}" style="width:300px;height:auto;" onclick="window.open(this.src)" /></div>'
                
                # 3. Attach to Report using 'extras'
                extra = getattr(report, "extras", [])
                extra.append(extras.html(html_image))
                report.extra = extra