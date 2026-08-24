import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс страницы авторизации интернет-магазина."""

    def __init__(self, driver: WebDriver, wait: WebDriverWait) -> None:
        """
        Инициализация элементов страницы авторизации.

        :param driver: Экземпляр WebDriver для управления браузером.
        :param wait: Экземпляр WebDriverWait для явных ожиданий элементов.
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = wait
        self.username_input: tuple[str, str] = (By.ID, "user-name")
        self.password_input: tuple[str, str] = (By.ID, "password")
        self.login_button: tuple[str, str] = (By.ID, "login-button")

    @allure.step("Авторизация пользователя с логином: '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему,
        ожидая появления поля ввода имени пользователя,
        после чего заполняет форму авторизации и нажимает кнопку Login.

        :param username: Строка с именем пользователя (логином).
        :param password: Строка с паролем пользователя.
        :return: None
        """
        self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
