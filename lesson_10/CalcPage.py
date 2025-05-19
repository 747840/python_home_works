from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """Это класс для страницы калькулятора, который содержит методы для взаимодействия с элементами:
     полем ввода задержки (локатор #delay), кнопками калькулятора (цифры, операторы, кнопка =),
     полем вывода результата"""

    def __init__(self, driver):
        """Эта функция открывает браузер, переходит на главную страницу сайта,
                 устанавливает глобальное ожидание и разворачивает окно браузера на весь экран"""
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium"
                         "-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay_input(self, waits : int) -> int:
        """Эта функция удаляет данные из поля ввода задержки и заполняет ее новыми данными"""
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(waits)

    def click_button_1(self, button_text) -> int:
        """Эта функция кликает на цифру калькулятора"""
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def click_button_2(self, button_text) -> str:
        """Эта функция кликает на оператор калькулятора"""
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def click_button_3(self, button_text) -> int:
        """Эта функция кликает на цифру калькулятора"""
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def click_button_4(self, button_text) -> None:
        """Эта функция кликает на кнопку = калькулятора"""
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def result(self, res : int) -> int:
        """Эта функция показывает результат в поле вывода результата после заданной задержки"""
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(EC.text_to_be_present_in_element
                     ((By.CLASS_NAME, "screen"), '15'))
        result = self._driver.find_element(By.CLASS_NAME, "screen").text
        assert int(result) == res