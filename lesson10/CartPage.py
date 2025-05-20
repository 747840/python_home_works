from selenium.webdriver.common.by import By


class CartPage:
    """Это класс для страницы корзины, который содержит метод
     для нажатия кнопки Checkout"""

    def __init__(self, browser):
        self._driver = browser

    def checkout_cart(self) -> None:
        """Эта функция для нажатия кнопки Checkout"""
        self._driver.find_element(By.ID, "checkout").click()
