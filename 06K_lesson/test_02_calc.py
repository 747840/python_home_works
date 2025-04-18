from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                    install()))
    driver.get(
        " https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    waiter = WebDriverWait(driver, 50)
    waiter.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), '15')
    )
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert int(result) == 15
