#Working with inline frames
from selenium import webdriver
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://www.selenium.dev/selenium/docs/api/java/index.html"
driver.get(url)

driver.switch_to.frame("packageListFrame")       #switch to frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(5)

driver.switch_to.default_content()               #return to default frame
time.sleep(2)

driver.switch_to.frame("packageFrame")           #switch to second frame
driver.find_element_by_link_text("Alert").click()
time.sleep(5)

driver.switch_to.default_content()
time.sleep(2)

driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("DEPRECATED").click()
