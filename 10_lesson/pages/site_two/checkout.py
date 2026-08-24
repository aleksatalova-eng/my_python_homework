import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс страницы оформления заказа."""

    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        """
        Инициализация локаторов элементов страницы оформления заказа.

        :param driver: Экземпляр WebDriver для управления браузером.
        :param wait: Экземпляр WebDriverWait для работы с ожиданиями.
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = wait
        self.first_name: tuple[str, str] = (By.ID, "first-name")
        self.last_name: tuple[str, str] = (By.ID, "last-name")
        self.postal_code: tuple[str, str] = (By.ID, "postal-code")
        self.continue_button: tuple[str, str] = (By.ID, "continue")
        self.total_label: tuple[str, str] = (
            By.CLASS_NAME, "summary_total_label")

    @allure.step(
            "Заполнение данных доставки:"
            "имя '{first_name}',"
            "фамилия '{last_name}',"
            "индекс '{postal_code}'")
    def fill_shipping_info(self, first_name: str,
                           last_name: str, postal_code: str) -> None:
        """
        Заполняет форму персональных данных покупателя для отправки заказа.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс адреса доставки.
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    @allure.step(
            "Подтверждение информации о доставке (нажатие кнопки Continue)")
    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения для перехода на следующий этап оформления.

        :return: None
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получение текста итоговой стоимости заказа")
    def get_total_price_text(self) -> str:
        """
        Ожидает видимости элемента с финальной стоимостью и
        возвращает его текстовое содержимое.

        :return: Строка (str) с текстом итоговой цены
        (например, "Total: $58.29").
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text
