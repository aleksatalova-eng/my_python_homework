import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для взаимодействия со страницей медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует объект страницы калькулятора.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver: WebDriver = driver
        self.url: str = (
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self._delay_input: tuple[str, str] = (By.ID, "delay")
        self._screen: tuple[str, str] = (By.CLASS_NAME, "screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> "CalculatorPage":
        """
        Открывает URL страницы калькулятора в браузере.

        :return: Текущий экземпляр класса CalculatorPage.
        """
        self.driver.get(self.url)
        return self

    @allure.step("Установить задержку: {seconds_str} сек.")
    def set_delay(self, seconds_str: str) -> "CalculatorPage":
        """
        Устанавливает задержку выполнения операций в секундах.

        :param seconds_str:
        Строковое значение секунд задержки (например, "45").
        :return: Текущий экземпляр класса CalculatorPage.
        """
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds_str)
        return self

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> "CalculatorPage":
        """
        Кликает по кнопке калькулятора с указанным текстом.

        :param button_text:
        Текст на кнопке калькулятора (например, "7", "+", "=").
        :return: Текущий экземпляр класса CalculatorPage.
        """
        locator: tuple[str, str] = (
            By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()
        return self

    @allure.step("Получить текст с экрана калькулятора")
    def get_screen_text(self) -> str:
        """
        Получает текущий текст, отображаемый на экране калькулятора.

        :return: Строка с текстом экрана калькулятора.
        """
        return self.driver.find_element(*self._screen).text

    @allure.step("Ожидать появление результата '{expected_text}' на экране")
    def wait_for_result(
            self, expected_text: str, timeout: int = 50) -> "CalculatorPage":
        """
        Ожидает появления ожидаемого текста на экране калькулятора.

        :param expected_text: Ожидаемый текст или результат на экране.
        :param timeout:
        Максимальное время ожидания в секундах (по умолчанию 50).
        :return:
        Текущий экземпляр класса CalculatorPage для поддержки цепочки вызовов.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
        return self
