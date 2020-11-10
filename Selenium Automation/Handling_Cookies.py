from selenium import webdriver
from time import sleep

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://www.amazon.in/")

"""#Fetch Cookies
cookies=driver.get_cookies() #get_cookie collects first cookie,but get_cookies collects all cookies
#print(cookies)
print(len(cookies))"""

"""#Add Cookies
new_cookie={"name":"VSSUT","value":"Burla"}
driver.add_cookie(new_cookie)
cookies=driver.get_cookies()
#print(cookies)
print(len(cookies))"""

"""#Delete Cookies
driver.delete_cookie("VSSUT")
cookies=driver.get_cookies()
print(len(cookies))
#print(cookies)"""

#Deleting all cookies
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
cookies=driver.delete_all_cookies()
print((cookies))