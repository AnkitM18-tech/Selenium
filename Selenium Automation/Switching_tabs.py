#Switch between tabs
from selenium import webdriver
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://rifinder.com/"
driver.get(url)
time.sleep(5)

driver.find_element_by_xpath("//*[@id='content']/article/div/div/div/div/section[7]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div/div[3]/a").click()
time.sleep(5)

tabs=driver.window_handles             #driver.current_window_handle() returns current window handle id

for tab in tabs:
    driver.switch_to.window(tab)
    print(driver.current_url)