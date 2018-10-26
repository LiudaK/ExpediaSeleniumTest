from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _account_link = "header-account-menu"
    _login_link = "account-signin"
    _email_field = "gss-signin-email"
    _password_field = "gss-signin-password"
    _login_button = "gss-signin-submit"

    # def getAccountLink(self):
    #     return self.driver.find_element(By.ID, self._account_link)
    #
    # def getLoginLink(self):
    #     return self.driver.find_element(By.ID, self._login_link)
    #
    # def getEmailLink(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordLink(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    def clickAccountLink(self):
        self.elementClick(self._account_link, locatorType="id")

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="id")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email, password):
        self.clickAccountLink()
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.driver.implicitly_wait(0.5)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[contains(text(), 'Hello')]", "xpath")
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent("signInEmailErrorMessage", "id")
        return result
