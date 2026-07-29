import allure
from selenium import webdriver
from pages.site_one.calculator import CalculatorPage


@allure.feature("Операции калькулятора")
@allure.story("Сложение на медленном калькуляторе")
@allure.title("Проверка сложения двух чисел с задержкой")
@allure.description(
    "Тест открывает калькулятор, выставляет задержку в 45 секунд, "
    "складывает 7 и 8, после чего ожидает результат 15."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    # Отдельный шаг для инициализации браузера
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    calcul_page = CalculatorPage(driver)

    # Разметка цепочки вызовов через шаги Allure
    with allure.step("Выполнить математическую операцию: 7 + 8"):
        calcul_page.open()\
            .set_delay("45")\
            .click_button("7")\
            .click_button("+")\
            .click_button("8")\
            .click_button("=")

    with allure.step(
            "Ожидать появление результата '15' на экране калькулятора"):
        calcul_page.wait_for_result("15")

    # Разметка итоговой проверки
    with allure.step("Проверить, что итоговое значение на экране равно '15'"):
        final_text = calcul_page.get_screen_text()
        assert final_text == "15"

    # Закрытие браузера в конце шага
    with allure.step("Закрыть браузер"):
        driver.quit()
