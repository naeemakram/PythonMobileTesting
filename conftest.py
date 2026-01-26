import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
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
    appium_server_url = "http://localhost:4723"

    # 3. Initialize Driver
    # Converts capabilities to options object and creates the driver.
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)

    # 4. Yield Driver to Test
    # The test runs here.
    yield driver

    # 5. Teardown
    # This runs after the test is finished.
    driver.quit()
