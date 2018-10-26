from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging

class SeleniumDriver():
    log =cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + ", locator type: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + ", locator type: " + locatorType)
        return element

    def elementClick(self, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + ", locator type: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator + ", locator type: " + locatorType)

    def sendKeys(self, data, locator, locatorType = "id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send data on element with locator: " + locator + ", locator type: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator + ", locator type: " + locatorType)


    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found with locator: " + locator + ", locator type: " + locatorType)
                return True
            else:
                self.log.error("Element not found with locator: " + locator + ", locator type: " + locatorType)
                return False
        except:
            self.log.error("Element not found with locator: " + locator + ", locator type: " + locatorType)
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Elements Found with locator: " + locator + ", locator type: " + byType)
                return True
            else:
                self.log.error("Elements not found with locator: " + locator + ", locator type: " + byType)
                return False
        except:
            self.log.error("Elements not found with locator: " + locator + ", locator type: " + byType)
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page with locator: " + locator + ", locator type: " + locatorType)
        except:
            self.log.error("Element not appeared on the web page with locator: " + locator + ", locator type: " + locatorType)
            print_stack()
        return element

