import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Класс главной страницы магазина (каталога)."""

    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        """
        Инициализация элементов страницы каталога товаров.

        :param driver: Экземпляр WebDriver для управления браузером.
        :param wait: Экземпляр WebDriverWait для явных ожиданий элементов.
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = wait
        self.cart_link: tuple[str, str] = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товара в корзину по идентификатору: '{item_id}'")
    def add_item_to_cart(self, item_id: str) -> None:
        """
        Динамически формирует локатор кнопки товара по его ID,
        ожидает кликабельности и добавляет в корзину.

        :param item_id:
        Строковый идентификатор (ID) кнопки добавления конкретного товара.
        :return: None
        """
        locator: tuple[str, str] = (By.ID, item_id)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Переход на страницу корзины")
    def go_to_cart(self) -> None:
        """
        Выполняет клик по иконке корзины для просмотра выбранных товаров.

        :return: None
        """
        self.driver.find_element(*self.cart_link).click()
