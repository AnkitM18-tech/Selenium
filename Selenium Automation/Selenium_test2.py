from selenium import webdriver
import time

#Path to the chromedriver
path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

#Opening the Url
url="https://rifinder.com/"
driver.get(url)

courses=driver.find_element_by_link_text("Courses")
courses.click()                #always remember to click on the link after initializing the variable.
time.sleep(6)
print(driver.current_url)    #to print current url.
driver.back()                #to navigate back to previous page.
#driver.forward()            #to navigate forward to next page.

#If there are previously something written we can use "(segment_name).clear()" to clear the texts.
"""url="https://www.selenium.dev/"
driver.get(url)
search=driver.find_element_by_id("gsc-i-id1")  #first look for ids,then class then others.
search.clear()     #clear the (previously default)/previous content.
time.sleep(5)
search.send_keys("test")                       #to send the data to search bar.
search.send_keys(Keys.RETURN)"""