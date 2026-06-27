from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = driver.find_element(By.CSS_SELECTOR, "#start > button")
    start_button.click()

    hello_text_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish > h4"))
    )

    actual_text = hello_text_element.text
    driver.save_screenshot("screenshot.png")

    assert actual_text == "Hello World!"

    driver.quit()
