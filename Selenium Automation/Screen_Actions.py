from selenium import webdriver
from time import sleep

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://rifinder.com/"
driver.get(url)


#Maximize Window
driver.maximize_window()
sleep(5)
#Scrolling Down the Page

#scroll down by pixel
#driver.execute_script("window.scrollBy(0,1500)"," ")  #Uses JS code...window.scrollBy(start pixel,end pixel)

#scroll down to the end of the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll to the end

#scroll down till an element is found
target=driver.find_element_by_xpath("//*[@id='content']/article/div/div/div/div/section[3]/div[3]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[1]/div/div/div/h3")
driver.execute_script("arguments[0].scrollIntoView();",target) # ; as it is JS code