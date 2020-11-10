from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://rifinder.com/"
driver.get(url)

register=driver.find_element_by_link_text("REGISTER NOW")
register.click()

new_account=driver.find_element_by_link_text("Create a new account")
new_account.click()
time.sleep(3)

input_tag=driver.find_elements_by_tag_name("input")
print(len(input_tag))

firstname=driver.find_element_by_name("first_name")
firstname.send_keys("Ankit")

lastname=driver.find_element_by_name("last_name")
lastname.send_keys("Nautiyal")

username=driver.find_element_by_name("user_login")
username.send_keys("Mofo")

email=driver.find_element_by_name("email")
email.send_keys("support@rifinder.com")

password=driver.find_element_by_name("password")
password.send_keys("madafaka")

confirm_password=driver.find_element_by_name("password_confirmation")
confirm_password.send_keys("madafaka")

time.sleep(1)
register_button=driver.find_element_by_class_name("tutor-button")
register_button.click()
