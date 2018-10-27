
"""
How to add PYTHONPATH to environment variable
Windows:
http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7
Mac:
http://stackoverflow.com/questions/3387695/add-to-python-path-mac-os-x
http://pytest-ordering.readthedocs.io/en/develop/
"""
from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import utilities.custom_logger as cl
import logging
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("luda4utest@gmail.com", "passwordabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("1", "1")
        result = self.lp.verifyLoginFail()
        assert result == True







