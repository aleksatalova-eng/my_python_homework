from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

    for name, value in form_data.items():
        input_field = driver.find_element(By.NAME, name)
        input_field.send_keys(value)

    driver.find_element(By.NAME, "zip-code").clear()

    submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))
    )

    zip_field = driver.find_element(By.ID, "zip-code")
    zip_class = zip_field.get_attribute("class")
    assert "alert-danger" in zip_class, (
        "Поле Zipcode подсвечено красным!"
    )

    for name in form_data.keys():
        field = driver.find_element(By.ID, name)
        field_class = field.get_attribute("class")
        assert "alert-success" in field_class, (
            "Все поля, кроме Zipcode, подсвечены зеленым!"
        )

    driver.quit()
