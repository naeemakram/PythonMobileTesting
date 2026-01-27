from pages.calculator_page import CalculatorPage

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
    calc_page.tap_two()
    calc_page.tap_multiply()
    calc_page.tap_two()
    calc_page.tap_equals()
    
    # 3. Assert (Validation stays in the test file)
    result = calc_page.get_result()
    assert result == "4"

def test_subtraction(driver):
    calc_page = CalculatorPage(driver)
    calc_page.tap_four()
    calc_page.tap_subtract()
    calc_page.tap_two()
    calc_page.tap_equals()
    result = calc_page.get_result()
    assert result == "2"

def test_division(driver):
    calc_page = CalculatorPage(driver)
    calc_page.tap_four()
    calc_page.tap_divide()
    calc_page.tap_two()
    calc_page.tap_equals()
    result = calc_page.get_result()
    assert result == "2"