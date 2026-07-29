import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.site_two.login import LoginPage
from pages.site_two.inventory import InventoryPage
from pages.site_two.cart import CartPage
from pages.site_two.checkout import CheckoutPage


@allure.title("Сквозной сценарий покупки товаров в магазине Swag Labs")
@allure.description(
    "Тест проверяет полный цикл покупки: авторизацию пользователя, "
    "добавление трех товаров в корзину, валидацию количества позиций, "
    "заполнение адреса доставки"
    "финальную проверку итоговой стоимости заказа.")
@allure.feature("Оформление заказа (Checkout)")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_shop_pom():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 300)

    with allure.step("Открытие главной страницы сайта"):
        driver.get("https://www.saucedemo.com/")

    # Инициализация страниц
    login_page = LoginPage(driver, wait)
    inventory_page = InventoryPage(driver, wait)
    cart_page = CartPage(driver, wait)
    checkout_page = CheckoutPage(driver, wait)

    # 1. Авторизация
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавление товаров в корзину
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")

    with allure.step("Переход со страницы каталога в корзину"):
        inventory_page.go_to_cart()

    # 3. Проверка содержимого корзины и нажатие Checkout
    with allure.step("Проверка: количество товаров в корзине равно 3"):
        assert cart_page.get_items_count() == 3

    cart_page.click_checkout()

    # 4. Оформление заказа и проверка стоимости
    checkout_page.fill_shipping_info("Александра", "Aлексеева", "640031")
    checkout_page.click_continue()

    # Проверка итоговой стоимости
    with allure.step(
            "Проверка: итоговая стоимость заказа составляет 'Total: $58.29'"):
        assert checkout_page.get_total_price_text() == "Total: $58.29"

    with allure.step("Закрытие сессии веб-драйвера"):
        driver.quit()
