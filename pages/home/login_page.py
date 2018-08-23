from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def login(self, username, password):
        account = self.driver.find_element(By.ID, "header-account-menu")
        account.click()
        login = self.driver.find_element(By.ID, "account-signin")
        login.click()

        usernameLink = self.driver.find_element(By.ID, "signin-loginid")
        usernameLink.send_keys(username)
        passwordLink = self.driver.find_element(By.ID, "signin-password")
        passwordLink.send_keys(password)

        submitbutton = self.driver.find_element(By.ID, "submitButton")
        submitbutton.click()
