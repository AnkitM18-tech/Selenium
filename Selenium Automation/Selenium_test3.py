from selenium import webdriver

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://rifinder.com/"
driver.get(url)

#X_Path  (driver.find_element_by_xpath("//div[@-----='----']"))
"""dashboard=driver.find_element_by_link_text("Dashboard")
dashboard.click()

new_account=driver.find_element_by_link_text("Create a new account")
new_account.click()

user_name=driver.find_element_by_name("user_login")
print(user_name.is_displayed())
print(user_name.is_enabled())"""

driver.implicitly_wait(5)              #Implicit Wait for all following commands.It will wait
                                       #max (5) secs for every command.

courses=driver.find_element_by_link_text("BROWSE COURSES")
courses.click()

course_select=driver.find_element_by_link_text("Whatsapp Automation using Python")
course_select.click()

return_back=driver.find_element_by_xpath("//li[@id='menu-item-488']")
return_back.click()