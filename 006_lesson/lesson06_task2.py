from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                install()))

driver.get("http://uitestingplayground.com/textinput")
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
                                ((By.ID, "updatingButton"), "SkyPro"))
txt = button.text
print(txt)
