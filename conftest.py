import datetime
import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path

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
    appium_server_url = "http://localhost:4723"

    # 3. Initialize Driver
    # Converts capabilities to options object and creates the driver.
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)

    # Attach the driver to the test item
    if request.node is not None:
        request.node.driver = driver

    # 4. Yield Driver to Test
    # The test runs here.
    yield driver

    # 5. Teardown
    # This runs after the test is finished.
    driver.quit()

# 2. THE SCREENSHOT HOOK (New Logic)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This runs after every test stage (setup, call, teardown).
    It checks if the test failed and takes a screenshot.
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # We only care if the actual test execution ("call") failed
    if report.when == "call" and report.failed:
        # Check if the test has a 'driver' attached
        driver = getattr(item, "driver", None)
        
        if driver:
            # Create a Path object for the screenshots directory
            screenshot_dir = Path("screenshots")
            
            # Create screenshots folder if missing
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate unique filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")                        
            file_path = screenshot_dir / f"FAIL_{item.name}_{timestamp}.png"

            # Take the screenshot
            driver.save_screenshot(str(file_path))
            
            # OPTIONAL: Attach to HTML Report (if using pytest-html)
            if "pytest_html" in item.config.pluginmanager.list_plugin_distinfo():
                extra = getattr(report, "extra", [])
                # (You can add logic here to embed image in report later)