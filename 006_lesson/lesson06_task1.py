from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                install()))
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
content = driver.find_element(By.CSS_SELECTOR, "#content")
wait = WebDriverWait(driver, 20)
success_element = wait.until(EC.visibility_of_element_located
                             ((By.CSS_SELECTOR, "p.bg-success")))
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)
