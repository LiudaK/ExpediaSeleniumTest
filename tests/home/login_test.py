
"""
How to add PYTHONPATH to environment variable
Windows:
http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7
Mac:
http://stackoverflow.com/questions/3387695/add-to-python-path-mac-os-x
"""
from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import utilities.custom_logger as cl
import logging
import pytest

class LoginTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    baseURL = "https://www.expedia.com/"
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.implicitly_wait(0.5)
    lp = LoginPage(driver)

    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.driver.get(self.baseURL)
    #     self.lp.login("1", "1")
    #     result = self.lp.verifyLoginFail()
    #     assert result == True
    #     self.driver.quit()

    #@pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("luda4utest@gmail.com", "passwordabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()






