import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс страницы корзины."""

    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        """
        Инициализация элементов страницы корзины.

        :param driver: Экземпляр WebDriver для управления браузером.
        :param wait: Экземпляр WebDriverWait для явных ожиданий элементов.
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = wait
        self.checkout_button: tuple[str, str] = (By.ID, "checkout")
        self.cart_item: tuple[str, str] = (By.CLASS_NAME, "cart_item")

    @allure.step("Переход к оформлению заказа (нажатие кнопки Checkout)")
    def click_checkout(self) -> None:
        """
        Ожидает кликабельности кнопки Checkout и нажимает на нее.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    @allure.step("Получение количества товаров в корзине")
    def get_items_count(self) -> int:
        """
        Находит все элементы товаров в корзине и
        возвращает их общее количество.

        :return: Целое число (int) — количество найденных элементов в корзине.
        """
        return len(self.driver.find_elements(*self.cart_item))
