from selenium.webdriver.common.by import By

class AuthorizationPage:
    """Этот класс для страницы авторизации, который содержит методы
     для ввода логина и пароля,а также для нажатия кнопки входа"""

    def __init__(self, driver):
        """Эта функция открывает браузер, переходит на главную страницу сайта,
         устанавливает глобальное ожидание и разворачивает окно браузера на весь экран"""
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(15)
        self._driver.maximize_window()

    def authorization(self, user : str, password : str) -> None:
        """Эта функция на странице авторизации вводит логин и пароль,
         и нажимает кнопку входа."""
        self._driver.find_element(By.ID, "user-name").send_keys(user)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()