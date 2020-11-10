from selenium import webdriver
from selenium.webdriver.support.ui import Select

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://www.facebook.com/r.php"
driver.get(url)

first_name=driver.find_element_by_id("u_0_n")
first_name.send_keys("Selenium")

surname=driver.find_element_by_id("u_0_p")
surname.send_keys("Dev Test")

email_address=driver.find_element_by_id("u_0_s")
email_address.send_keys("support@rifinder.com")

re_enter_email=driver.find_element_by_id("u_0_v")
re_enter_email.send_keys("support@rifinder.com")

password=driver.find_element_by_id("password_step_input")
password.send_keys("xxx729576")

gender=driver.find_element_by_id("u_0_5")
verify_gender=gender.is_selected()
if  verify_gender != True:
    gender=driver.find_element_by_id("u_0_5")
    gender.click()

day=Select(driver.find_element_by_id("day"))    #as it's in select tag,we have to call Select class here
#select_by_visible_text
day.select_by_visible_text("18")

month=Select(driver.find_element_by_id("month"))
#selecting by index
month.select_by_index("3")

year=Select(driver.find_element_by_id("year"))
#select by value
year.select_by_value("2000")

signup=driver.find_element_by_id("u_0_14")
signup.click()