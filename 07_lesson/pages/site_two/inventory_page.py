from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Класс главной страницы магазина (каталога)."""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_id):
        locator = (By.ID, item_id)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
