#Importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#------------------------------------------------------------------------------------------------
#Open Browser
path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)
#------------------------------------------------------------------------------------------------
#open any desired website
"""url="https://animepahe.com/"
driver.get(url)"""
#driver.close()  #close the tab
#driver.quit()   #close the browser
#print(driver.title)  #print the title of page
#------------------------------------------------------------------------------------------------
#Load Elements using Selenium
url="https://www.selenium.dev/"
driver.get(url)
"""download=driver.find_element_by_link_text("Downloads")
download.click()                               #to click on the link
search=driver.find_element_by_id("gsc-i-id1")  #first look for ids,then class then others.
search.send_keys("test")                   #to send the data to search bar.
search.send_keys(Keys.RETURN)"""             #to hit return(enter).
#print(driver.page_source)                  #to get the source code.
#-------------------------------------------------------------------------------------------------
#Saving the search result
search=driver.find_element_by_id("gsc-i-id1")  #first look for ids,then class then others.
search.send_keys("test")                       #to send the data to search bar.
search.send_keys(Keys.RETURN)
#search_result=driver.find_element_by_class_name("gsc-wrapper")
#print(search_result.text)
#--------------------------------------------------------------------------------------------------
#Explicit Wait
try:
    search_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gsc-wrapper"))
    )
    print(search_result.text)
except:
    driver.quit()
#--------------------------------------------------------------------------------------------------