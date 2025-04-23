from selenium.webdriver.common.by import By


class AuthorizationPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def authorization(self, user, password):
        self._driver.find_element(By.ID, "user-name").send_keys(user)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
