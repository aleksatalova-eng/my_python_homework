from selenium import webdriver
from pages.site_one.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()

    calcul_page = CalculatorPage(driver)

    calcul_page.open()\
        .set_delay(45)\
        .click_button("7")\
        .click_button("+")\
        .click_button("8")\
        .click_button("=")\
        .wait_for_result("15")

    assert calcul_page.get_screen_text() == "15"

    driver.quit()
