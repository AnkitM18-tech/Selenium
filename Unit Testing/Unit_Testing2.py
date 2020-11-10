from selenium import webdriver
import unittest

class testCase(unittest.TestCase):
    def setUp(self):
        path="C:/Users/OCAC/Desktop/Selenium/chromedriver.exe"
        self.driver=webdriver.Chrome(path)
        url="https://rifinder.com/"
        self.driver.get(url)

        #assertIsNone() and assertIsNotNone()
        #assertIsNone(var) returns True(OK) if var is None.assertIsNotNone(var) is opposite.
        #self.assertIsNone(self.driver)

    #assertTrue and assertFalse(just remove not)
    def not_test_Assertion(self):
        title=self.driver.title
        self.assertTrue(title=="RiFinder - Learn | Code | Share") #assertFalse() return False if condition is True.
                                                                                       #(Assertion Error)
    #assertEqual and assertNotEqual(just remove not)
    def not_test_Assertion2(self):
        title=self.driver.title
        self.assertEqual("RiFinder - Learn | Code | Share",title,"Title not matched")
        #Three arguments.(target match,variable,in case of error message).
        #It runs fine if variable=target match. assertNotEqual(target,variable) opposite of assertEqual().

    #assertGreater and assertLess(just remove not)
    def test_Assertion3(self):
        self.assertGreater(100,10)   # a>b--->returns True ,GreaterEqual-->a>=b. assertLess
        # and LessEqual is opposite.
        self.assertGreaterEqual(10,10)
        self.assertLess(3,8)
        self.assertLessEqual(100,100)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()