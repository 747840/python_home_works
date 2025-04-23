from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def checkout_cart(self):
        self._driver.find_element(By.ID, "checkout").click()
