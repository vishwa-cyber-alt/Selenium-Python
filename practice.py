from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.website.com/sign-in/?source=SC&country=IN")
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("student")
password=driver.find_element(By.ID,"password")
password.send_keys("Password123")
button = driver.find_element(By.ID, "signin-submit2")
button.click();




