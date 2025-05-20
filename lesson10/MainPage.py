from selenium.webdriver.common.by import By


class MainPage:
    """Это класс для главной страницы магазина, который содержит методы для
     добавления товаров в корзину и перехода в корзину"""

    def __init__(self, browser):
        self._driver = browser

    def add_to_cart(self) -> None:
        """Эта функция добавляет товар в корзину"""
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-bolt-t-shirt"
                                  ).click()
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """Эта функция осуществляет переход в корзину"""
        self._driver.find_element(By.ID, "shopping_cart_container").click()
