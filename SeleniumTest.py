import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumTest:

    def __init__(self, url):
        self.driver = webdriver.Firefox(executable_path=f"{os.getcwd()}/geckodriver")
        self.action = ActionChains(self.driver)
        self.driver.get(url)

    def getDriver(self):
        return self.driver

    def getPage(self):
        return self.driver.page_source

    def getUrl(self):
        return self.driver.current_url

    def click(self, xpath):
        element = self.getElementByXPath(xpath)
        element.click()
    
    def sendKeys(self, xpath, keys):
        element = self.getElementByXPath(xpath)
        element.send_keys(keys)
    
    def getElementByXPath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        if element:
            return element

    def getElementByID(self, id):
        element = self.driver.find_element_by_id(id)
        if element:
            return element

    def moveToElement(self, xpath):
        element = self.getElementByXPath(xpath)
        self.action.move_to_element(element).perform()

    def closeTab(self):
        self.driver.close()

    def closeDriver(self):
        self.driver.quit()

    def changeToNextWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
