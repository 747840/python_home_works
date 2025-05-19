import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from AuthorizationPage import AuthorizationPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


@allure.title("Проверка функциональности интернет-магазина")
@allure.description("Оформление заказа")
@allure.feature("Проверка итоговой суммы")
@allure.severity("blocker")
def test_purchase():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().
                                               install()))

    with allure.step("Открыть страницу авторизации"):
        authorization = AuthorizationPage(browser)
    with allure.step("Ввести логин и пароль"):
        authorization.authorization("standard_user", "secret_sauce")
    with allure.step("Открыть страницу с товаром"):
        main_page = MainPage(browser)
    with allure.step("Выбрать товар"):
        main_page.add_to_cart()
    with allure.step("Перейти в корзину"):
        main_page.go_to_cart()
    with allure.step("Открыть корзину"):
        cart_page = CartPage(browser)
    with allure.step("Перейти к оформлению заказа"):
        cart_page.checkout_cart()
    with allure.step("Открыть страницу заполнения формы"):
        order_page = OrderPage(browser)
    with allure.step("Заполнить форму"):
        order_page.form_data("Снежана", "Матвеева", 625501)
    with allure.step("Проверить заказ"):
        order_page = OrderPage(browser)
    with allure.step("Проверить итоговую сумму"):
        order_page.total_cost()

    browser.quit()
