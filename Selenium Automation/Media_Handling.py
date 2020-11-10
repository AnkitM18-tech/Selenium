from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_opt=Options()      #creating option object
prefs={"download.default_directory":"C://Users/OCAC/Downloads//","directory_upgrade":True}
chrome_opt.add_experimental_option("prefs",prefs)#changing default path

path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path,options=chrome_opt)

"""#Upload Files
driver=webdriver.Chrome(path)
driver.get("https://tus.io/demo.html")
driver.maximize_window()

choose_file=driver.find_element_by_xpath("//*[@id='js-file-input']")
choose_file.send_keys("C:/Users/OCAC/Downloads/Ganesha/1.jpg")
sleep(15)
#C:/Users/OCAC/Downloads/Ganesha/1.jpg

#showing the file in that window(on that demo site)
full_size_img=driver.find_element_by_xpath('//*[@id="js-upload-container"]/a[1]')
full_size_img.click()"""

"""#Downloading to default path
driver.get("http://demo.astra-net.com/download/")
driver.maximize_window()

target=driver.find_element_by_xpath('//*[@id="content_container"]/div/table/tbody/tr[9]/td[1]/a')
target.click()"""

#Download to specific path
driver.get("http://demo.astra-net.com/download/")
driver.maximize_window()

target=driver.find_element_by_xpath('//*[@id="content_container"]/div/table/tbody/tr[9]/td[1]/a')
target.click()