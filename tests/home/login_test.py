from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):
    def test_validloging(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(1)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("luda4utest@gmail.com", "passwordabc")

        flight = driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")
        if flight is not None:
            print("Login Successful")
        else:
            print("Login Faileed")


