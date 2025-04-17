import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_purchase(driver):
    # Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # sleep(5)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Снежана")
    driver.find_element(By.ID, "last-name").send_keys("Матвеева")
    driver.find_element(By.ID, "postal-code").send_keys(625501)
    driver.find_element(By.ID, "continue").click()
    # sleep(10)
    # Чтение итоговой стоимости
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

    # Проверка итоговой суммы
    assert total_cost_value == 58.29, (f"Итоговая сумма должна быть 58.29, но"
                                       f" получена {total_cost_value}")
