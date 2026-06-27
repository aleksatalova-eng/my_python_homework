from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():

    driver = webdriver.Chrome()

    cookie_user_1 = {
        'name': 'SESSION',
        'value': 'ZmNjODViMGMtYmY0OS00NjZmLWE2MDktZTRmMTAxNDM4Zjli',
        'domain': '.gitflic.ru'
    }

    cookie_user_2 = {
        'name': 'SESSION',
        'value': 'ZGVmY2YyOTgtODVjYS00Nzg3LWJiMzUtNDk5NTZmZGNiZDlj',
        'domain': '.gitflic.ru'
    }

    driver.get("https://gitflic.ru/")

    driver.add_cookie(cookie_user_1)

    driver.refresh()

    profile_link_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable
            ((By.XPATH, "//a[contains(@href, '/auth/login')]"))
        )
    profile_link_1.click()

    url_user_1 = driver.current_url
    print(f"URL Пользователя 1: {url_user_1}")

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")

    driver.add_cookie(cookie_user_2)

    driver.refresh()

    profile_link_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable
            ((By.XPATH, "//a[contains(@href, '/auth/login')]"))
        )
    profile_link_2.click()

    url_user_2 = driver.current_url
    print(f"URL Пользователя 2: {url_user_2}")

    assert url_user_1 != url_user_2
    print("Тест успешно пройден: URL пользователей различаются.")
    driver.quit()
