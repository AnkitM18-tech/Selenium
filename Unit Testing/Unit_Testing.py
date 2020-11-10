from unittest.case import skipIf
from selenium import webdriver
import unittest

class testCase(unittest.TestCase):
    def setUp(self):
        path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
        self.driver=webdriver.Chrome(path)
        url="https://rifinder.com/"
        self.driver.get(url)
    #all functions starting with 'test' will be performed.No of functions=no of executions of setUp().
    @unittest.SkipTest                  #decorator to skip the test.
    def test_First_Case(self):
        print("This is successful test case")

    def test_Second_Case(self):
        print("This is successful 2nd test case")

    @unittest.skip("It's not ready")     #another way to skip. @unittest.skipIf(condition)
    def test_Third_Case(self):
        print("This is successful 3rd test case")

    def not_Test_Case(self):          #it's not starting with 'test' word,so it's not executing
        print("This won't run")

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()