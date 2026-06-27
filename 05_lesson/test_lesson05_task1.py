from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

    forms_link = driver.find_element(By.LINK_TEXT, "HTML form")
    forms_link.click()
    assert "/forms/post" in driver.current_url
    driver.back()

    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
