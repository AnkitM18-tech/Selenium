"""
#Alert Box
from selenium import webdriver
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
driver.get(url)

alert_box=driver.find_element_by_xpath("//button[@onClick='myAlertFunction()']")
alert_box.click()

time.sleep(3)
alert_box_accept=driver.switch_to_alert()                   #to move to the alert box section
time.sleep(3)
alert_box_accept.accept()                     # we can directly use .accept() or can also create a variable.
"""
"""
#Confirmation Box
from selenium import webdriver
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
driver.get(url)

driver.refresh()
time.sleep(5)
confirmation_box=driver.find_element_by_xpath("//button[@onclick='myConfirmFunction()']")
confirmation_box.click()
time.sleep(3)
acceptance_box=driver.switch_to_alert()
time.sleep(2)
#acceptance_box.accept()             #For accepting.
acceptance_box.dismiss()            #For canceling.
"""
#Prompt Alert Box
from selenium import webdriver
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
driver.get(url)

#driver.refresh()          for refreshing the page.
#time.sleep(5)             time gap for refreshing.
prompt_box=driver.find_element_by_xpath("//button[@onclick='myPromptFunction()']")
prompt_box.click()
time.sleep(3)
prompt_box=driver.switch_to.alert
time.sleep(2)
prompt_box.send_keys("Ankit")
time.sleep(2)
prompt_box.accept()
#prompt_box.dismiss()