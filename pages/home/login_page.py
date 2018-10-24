from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
    #Locators
    _account_link = "header-account-menu"
    _login_link = "account-signin"
    _email_field = "gss-signin-email"
    _password_field = "gss-signin-password"
    _login_button = "gss-signin-submit"

    def getAccountLink(self):
        return self.driver.find_element(By.ID, self._account_link)

    def getLoginLink(self):
        return self.driver.find_element(By.ID, self._login_link)

    def getEmailLink(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordLink(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.ID, self._login_button)

    def clickAccountLink(self):
        self.getAccountLink().click()

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailLink().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordLink().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickAccountLink()
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
