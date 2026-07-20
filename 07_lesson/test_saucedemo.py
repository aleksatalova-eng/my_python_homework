from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.site_two.login_page import LoginPage
from pages.site_two.inventory_page import InventoryPage
from pages.site_two.cart_page import CartPage
from pages.site_two.checkout_page import CheckoutPage


def test_saucedemo_shop_pom():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 30)

    # Открытие сайта
    driver.get("https://www.saucedemo.com/")

    # Инициализация страниц
    login_page = LoginPage(driver, wait)

    # 1. Авторизация
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver, wait)
    cart_page = CartPage(driver, wait)
    checkout_page = CheckoutPage(driver, wait)
    # 2. Добавление товаров в корзину
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")

    # Переход в корзину
    inventory_page.go_to_cart()

    # 3. Проверка содержимого корзины и нажатие Checkout
    assert cart_page.get_items_count() == 3
    cart_page.click_checkout()

    # 4. Оформление заказа и проверка стоимости
    checkout_page.fill_shipping_info("Александра", "Aлексеева", "640031")
    checkout_page.click_continue()

    # Проверка итоговой стоимости
    assert checkout_page.get_total_price_text() == "Total: $58.29"

    driver.quit()
