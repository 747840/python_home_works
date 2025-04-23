from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self._driver = browser

    def add_to_cart(self):
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-bolt-t-shirt"
                                  ).click()
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        self._driver.find_element(By.ID, "shopping_cart_container").click()
