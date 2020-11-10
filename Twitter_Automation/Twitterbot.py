from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from time import sleep
import Password                 #make a Password.py file from which you want to retrieve the username and password

class twitter_bot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome("C:/Users/OCAC/Desktop/Selenium/chromedriver.exe")

    def login(self):
        driver=self.driver
        driver.get("https://twitter.com/login")
        driver.maximize_window()
        sleep(5)
        #login_start=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
        #login_start.click()
        user=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        user.clear()
        user.send_keys(self.username)
        password.clear()
        password.send_keys(self.password)
        login_button=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
        login_button.click()
        sleep(5)

    def likeTweet(self,searchfor):
        driver=self.driver
        search_box=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        search_box.send_keys(searchfor)
        search_box.send_keys(Keys.RETURN)
        sleep(8)
        for i in range(1,3):
            #try:
            driver.find_element_by_xpath("//div[@data-testid='like']").click()
            """#except exceptions.NoSuchElementException:
                sleep(3)
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight/2)') 
                sleep(3)
                driver.find_element_by_xpath("//div[@data-testid='like']").click()

            sleep(1)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight/2)')"""
            sleep(5)
            


pass_word=Password.Password()
username=Password.user_name()

find=twitter_bot(username,pass_word)
find.login()
find.likeTweet("selenium")
