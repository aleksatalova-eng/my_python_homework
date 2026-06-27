from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Александра")

    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit order')]")
    submit_button.click()

    assert driver.current_url == "https://httpbin.org/post"

    driver.quit()
