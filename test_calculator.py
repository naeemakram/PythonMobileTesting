import json
import os
from pages.calculator_page import CalculatorPage
import pytest

def test_addition(driver):
    
    # 1. Initialize the Page
    calc_page = CalculatorPage(driver)
    
    # 2. Perform Actions (Readable!)
    calc_page.tap_two()
    calc_page.tap_plus()
    calc_page.tap_two()
    calc_page.tap_equals()
    
    # 3. Assert (Validation stays in the test file)
    result = calc_page.get_result()
    assert result == "4"


def test_multiplication(driver):
    
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
    calc_page = CalculatorPage(driver)
    calc_page.tap_digit("4")
    calc_page.tap_subtract()
    calc_page.tap_digit("2")
    calc_page.tap_equals()
    result = calc_page.get_result()
    assert result == "2"

def test_division(driver):
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
    print(data_path)

    with open(data_path) as f:
        return json.load(f)
    
@pytest.mark.parametrize("data", load_test_data(), ids=lambda x: x["test_name"])
def test_addition_ddt(driver, data):
    """
    This test runs 3 times automatically (once for each block in the JSON).
    """
    print(f"\nRunning Test Case: {data['test_name']}")
    
    calc_page = CalculatorPage(driver)
    
    # Use the dynamic data
    calc_page.tap_digit(data["input_a"])
    calc_page.tap_plus()
    calc_page.tap_digit(data["input_b"])
    calc_page.tap_equals()
    
    # Assert
    assert calc_page.get_result() == data["expected"]