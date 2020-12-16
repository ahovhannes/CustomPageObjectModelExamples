#
#   UI Automation
#         Author: Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
# Testing server: http://blog.csssr.ru/qa-engineer/
#    Run Command: python csssr.com_Cases.py
#
# If the subpage's title isn't bold test execution will be break via assertion, otherways, testcase will finish wth success
#
import time
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.common.exceptions import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#import logging
##logging.basicConfig(filename='rezults2.log',level=logging.DEBUG)
#logging.basicConfig(filename='rezults.log',level=logging.INFO)


class myTestCase(unittest.TestCase):
    def setUp(self):
        self.site_url = "http://blog.csssr.ru/qa-engineer/"
        #
        # FOR WINDOWS
        testingBrowser = 'Firefox'
        testingBrowser = 'Chrome'
        if testingBrowser == 'Firefox':
            geckodriverPath="C:\\h\\USED\\Selenium_web_drivers\\Firefox"
            self.driver=webdriver.Firefox(geckodriverPath)
        elif testingBrowser == 'Chrome':
            geckodriverPath="C:\\h\\USED\\Selenium_web_drivers\\Chrome"+"\\chromedriver.exe"
            capabilities = DesiredCapabilities.CHROME
            capabilities['goog:loggingPrefs'] = { 'browser':'ALL' }
            self.driver=webdriver.Chrome(geckodriverPath, desired_capabilities=capabilities)
        else:
            self.my_print("..... ERROR: Wrong Browser type .....")
        #
        ## FOR LINUX
        #path = '/usr/local/bin/geckodriver'
        #profile = webdriver.FirefoxProfile()
        #self.driver = webdriver.Firefox(executable_path=path, firefox_profile=profile)
        ##self.driver.get(self.site_url)
        ##self.my_print(self.driver.title)
        #
        self.wait = WebDriverWait(self.driver, 10)
        self.probel2 = '  '
        self.probel4 = '    '
        self.probel8 = '        '
        self.logFile = 'rezults.log'
        #open(self.logFile, 'w').close()
        self.supPage2Link = '//div/a[contains(text(), "НАХОДИТЬ НЕСОВЕРШЕНСТВА")]'
        self.title2 = '/html/body/div[1]/section[2]/div[2]/h1'


    def tearDown(self):
        self.my_print("---------------------------------------------------------------------")
        self.driver.close()  ##Close the browser window that the driver has focus of
        #webDriver.Quit()    ##Calls Dispose()
        #webDriver.Dispose() ##Closes all browser windows and safely ends the session

    def test_cases(self):
        self.my_print("..... Opening the site "+self.site_url+" .....")
        self.driver.get(self.site_url)
        self.my_print("..... Executing Test-Cases .....\n")
        self.tc2('Is the checkbox readonly?')
        self.tc1('Checking if subpage title is bold')


    #Function for printing on console, or for logging into file
    def my_print(self, myText):
        print(myText)
        #
        import logging
        logging.basicConfig(filename=self.logFile,level=logging.INFO)
        logging.info(myText)
        #logging.error(myText)

    #This function will check web page element existance
    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True


    #Testcase1: Checking if subpage title is bold
    def tc1(self, testCaseName):        
        self.my_print(self.probel2+"----- Begin TestCase: "+testCaseName+" -----")
        if self.check_exists_by_xpath(self.supPage2Link):
            # Going to subpage2
            self.my_print(self.probel2+"..... Going to page2 .....")            
            self.driver.find_element_by_xpath(self.supPage2Link).click()
            # Chechink is the title bold
            isBold = self.driver.find_element_by_xpath(self.title2).get_attribute('font-weight')
            #if isBold:
            #    self.my_print(self.probel2+"SUCCESS: Title is bold")
            #else:
            #    self.my_print(self.probel2+"ERROR: Title isn't bold")
            assert isBold is not None, "ERROR: Title isn't bold"
            self.my_print(self.probel2+"SUCCESS: Title is bold")
        self.my_print(self.probel2+"----- END TestCase: "+testCaseName+" -----\n")


    #Testcase2: Checking if subpage title is bold
    def tc2(self, testCaseName):
        self.my_print(self.probel2+"----- Begin TestCase: "+testCaseName+" -----")
        pass
        self.my_print(self.probel2+"----- End TestCase: "+testCaseName+" -----\n")


if __name__ == "__main__":
    unittest.main()




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    