from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, browser):
        self._driver = browser

    def form_data(self, first, last, postal):
        self._driver.find_element(By.ID, "first-name").send_keys(first)
        self._driver.find_element(By.ID, "last-name").send_keys(last)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal)
        self._driver.find_element(By.ID, "continue").click()

    def total_cost(self):
        total_cost = self._driver.find_element(By.CLASS_NAME,
                                               "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])
        assert total_cost_value == 58.29, (f"Итоговая сумма должна быть"
                                           f" 58.29, но получена"
                                           f" {total_cost_value}")
