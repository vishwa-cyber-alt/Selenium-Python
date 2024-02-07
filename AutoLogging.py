# Python program to demonstrate
# selenium

# import webdriver
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search

# get geeksforgeeks.org
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

# get element 
element = driver.find_element(By.XPATH, '//*[@id="login-form"]/ul/li[1]')
element.send_keys("arery@yahoo.com") 
# print complete element

# send the username to the input field
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# find the username input field
username_input = driver.find_element(By.ID, "username")

# send the username to the input field
username_input.send_keys("student")
password=driver.find_element(By.ID,"password")
password.send_keys("Password123")

# find the second input field (e.g., password field)
button = driver.find_element(By.ID, "submit")
button.click();

#login-input-wrapper


