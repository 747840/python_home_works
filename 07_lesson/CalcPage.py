from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium"
                         "-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay_input(self, waits):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(waits)

    def click_button_1(self, button_text):
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def click_button_2(self, button_text):
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def click_button_3(self, button_text):
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def click_button_4(self, button_text):
        self._driver.find_element(By.XPATH,
                                  f"//span[contains(@class, 'btn') and"
                                  f" text()='{button_text}']").click()

    def result(self, res):
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(EC.text_to_be_present_in_element
                     ((By.CLASS_NAME, "screen"), '15'))
        result = self._driver.find_element(By.CLASS_NAME, "screen").text
        assert int(result) == res
