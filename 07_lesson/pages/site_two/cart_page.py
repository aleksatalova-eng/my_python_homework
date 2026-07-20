from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс страницы корзины."""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.checkout_button = (By.ID, "checkout")
        self.cart_item = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)).click()

    def get_items_count(self):
        return len(self.driver.find_elements(*self.cart_item))
