from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://practicetestautomation.com/practice-test-login/")
print("1 blog 2 contact")
input=int(input("enter = "))
if input==2:
    button = driver.find_element(By.ID, "menu-item-18")
    button.click();
elif input==1:
    button=driver.find_element(By.ID, "menu-item-19")
    button.click();



