from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

"""url="https://www.facebook.com/r.php"
driver.get(url)

month=Select(driver.find_element_by_id("month"))
all_month_options=month.options

for month in all_month_options:
    print(month.text)                                #printing all values of dropdown menu."""

#Finding all links available in a page.
url="https://rifinder.com/"
driver.get(url)
time.sleep(5)

links=driver.find_elements_by_tag_name("a")
print("The Total number of Links present are: ",len(links))

for link in links:
    print(link.text)                              #(.text) is necessary to extract just the link.
