from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)
input_field = driver.find_element(By.ID, "username")
input_field.send_keys("tomsmith")
sleep(2)
input_field = driver.find_element(By.ID, "password")
input_field.send_keys("SuperSecretPassword!")
sleep(2)
button = driver.find_element(By.CSS_SELECTOR, ".fa-2x")
button.click()
sleep(2)
message = driver.find_element(By.ID, "flash").text
print(message)
driver.quit()
