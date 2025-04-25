from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from AuthorizationPage import AuthorizationPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


def test_purchase():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().
                                               install()))

    authorization = AuthorizationPage(browser)
    authorization.authorization("standard_user", "secret_sauce")
    main_page = MainPage(browser)
    main_page.add_to_cart()
    main_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout_cart()

    order_page = OrderPage(browser)
    order_page.form_data("Снежана", "Матвеева", 625501)

    order_page = OrderPage(browser)
    order_page.total_cost()

    browser.quit()
