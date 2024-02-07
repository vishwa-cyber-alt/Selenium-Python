from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://phptravels.com/demo/")
button = driver.find_element(By.ID, "demo")
button.click();
