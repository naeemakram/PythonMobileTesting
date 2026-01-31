import json
import logging
import os
from pages.calculator_page import CalculatorPage
import pytest

# 1. Initialize Logger
LOGGER = logging.getLogger(__name__)

def test_addition(driver):
    LOGGER.info(f"\nRunning Test Case: test_addition 2+2=4")
    # 1. Initialize the Page
    calc_page = CalculatorPage(driver)
    
    # 2. Perform Actions (Readable!)
    calc_page.tap_digit("2")    
    calc_page.tap_plus()
    calc_page.tap_digit("2")
    calc_page.tap_equals()
    
    # 3. Assert (Validation stays in the test file)
    result = calc_page.get_result()
    assert result == "4"


def test_multiplication(driver):
    LOGGER.info(f"\nRunning Test Case: test_multiplication 2*2=4")
    # 1. Initialize the Page
    calc_page = CalculatorPage(driver)
    
    # 2. Perform Actions (Readable!)
    calc_page.tap_digit("2")
    calc_page.tap_multiply()
    calc_page.tap_digit("2")
    calc_page.tap_equals()
    
    # 3. Assert (Validation stays in the test file)
    result = calc_page.get_result()
    assert result == "4"

def test_subtraction(driver):
    LOGGER.info(f"\nRunning Test Case: test_subtraction 4-2=2")
    calc_page = CalculatorPage(driver)
    calc_page.tap_digit("4")
    calc_page.tap_subtract()
    calc_page.tap_digit("2")
    calc_page.tap_equals()
    result = calc_page.get_result()
    assert result == "2"

def test_division(driver):
    LOGGER.info(f"\nRunning Test Case: test_division 4/2=2")
    calc_page = CalculatorPage(driver)
    calc_page.tap_digit("4")
    calc_page.tap_divide()
    calc_page.tap_digit("2")
    calc_page.tap_equals()
    result = calc_page.get_result()
    assert result == "2"


# 1. Helper function to load the JSON file
def load_test_data():
    # Get absolute path to the 'data' folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level (..) to root, then into 'data'
    data_path = os.path.join(current_dir, "data", "test_data.json")
    LOGGER.info(f"Loading test data from: {data_path}")

    with open(data_path) as f:
        return json.load(f)
    
@pytest.mark.parametrize("data", load_test_data(), ids=lambda x: x["test_name"])
def test_addition_ddt(driver, data):
    """
    This test runs 3 times automatically (once for each block in the JSON).
    """
    LOGGER.info(f"Running Test Case: {data['test_name']}")
    LOGGER.info(f"{data["input_a"]} + {data["input_b"]} = {data["expected"]}")
    calc_page = CalculatorPage(driver)
    
    # Use the dynamic data
    calc_page.tap_digit(data["input_a"])
    calc_page.tap_plus()
    calc_page.tap_digit(data["input_b"])
    calc_page.tap_equals()
    
    # Assert
    assert calc_page.get_result() == data["expected"]