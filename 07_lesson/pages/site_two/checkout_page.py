from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс страницы оформления заказа."""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name)).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_total_price_text(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.total_label))
        return total_element.text
