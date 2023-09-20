import unittest
from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MyTestCase_index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(25)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()
        print("-----------------------------")
        print("Environment setup ready")
        print("Test run began at:" + str(datetime.datetime.now()))

    def test_mod(self):
        self.driver.get("http://13.48.84.148:8080")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,("body > div.row.text-left > div > nav > div > div:nth-child(5) > a")).click()
        sleep(2)

    def tearDown(self):
        if self.driver != None:
            print("--------------------------------")
            print("Test Environment Destroyed")
            print("Run completed at :" + str(datetime.datetime.now()))
            self.driver.close()

if __name__ == '__main__':
    unittest.main()
