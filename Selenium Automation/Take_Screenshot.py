from selenium import webdriver
from time import sleep

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://rifinder.com/"
driver.get(url)

driver.save_screenshot("Rifinder.png")
#driver.get_screenshot_as_file("-------path/file_name.extension")