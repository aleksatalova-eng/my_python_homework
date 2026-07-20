from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        # Локаторы элементов
        self._delay_input = (By.ID, "delay")
        self._screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)
        return self

    def set_delay(self, seconds_str):
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds_str)
        return self

    def click_button(self, button_text):
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()
        return self

    def get_screen_text(self):
        return self.driver.find_element(*self._screen).text

    def wait_for_result(self, expected_text, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
