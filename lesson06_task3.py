from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 40)
wait.until(
    EC.presence_of_element_located((By.ID, "landscape"))
)

images = driver.find_elements(By.CSS_SELECTOR, "#award")
src_value = driver.find_elements(By.CSS_SELECTOR, "#award")[0].get_dom_attribute("src")

print(src_value)
