from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)

url="https://www.toolsqa.com/selenium-webdriver/mouse-hover-action/"
driver.get(url)

#sleep(8)
#Mouse Hover
tutorials=driver.find_element_by_xpath("//*[@id='primary-menu']/li[2]/a/span/span")
#sleep(5)
practices=driver.find_element_by_xpath("//*[@id='primary-menu']/li[2]/ul/li[1]/a/span/span")
#sleep(5)
test=driver.find_element_by_xpath("//*[@id='primary-menu']/li[2]/ul/li[1]/ul/li[1]/a/span/span")

actions=ActionChains(driver)      #for hover actions
#sleep(5)
actions.move_to_element(tutorials).move_to_element(practices).move_to_element(test).click().perform()
#------------------------------------------------------------------------------
"""#Double click
url="http://demo.guru99.com/test/simple_context_menu.html"
driver.get(url)
sleep(3)
button=driver.find_element_by_xpath("//*[@id='authentication']/button")
actions=ActionChains(driver)

actions.double_click(button).perform()
sleep(5)"""
#------------------------------------------------------------------------------
"""#Right Click
url="http://demo.guru99.com/test/simple_context_menu.html"
driver.get(url)
sleep(3)
button=driver.find_element_by_xpath("//*[@id='authentication']/span[1]")
actions=ActionChains(driver)

actions.context_click(button).perform()
sleep(3)

driver.find_element_by_xpath("//*[@id='authentication']/ul/li[3]").click()"""
#------------------------------------------------------------------------------
"""#Drag and Drop
url="https://demos.telerik.com/jsp-ui/dragdrop/index"
driver.get(url)

sleep(3)
source_element=driver.find_element_by_xpath("//*[@id='draggable']")
target_element=driver.find_element_by_xpath("//*[@id='droptarget']")
actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()"""