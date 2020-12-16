#
# Author: Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
#
# Написать тестирование страницы авторизации: https://dev-shop.jowi.club/auth/sign-in
# Необходим скрипт, чтобы он автоматически открывал браузер заполнял данные, если возникает ошибка, то писал лог ошибки.
# Далее авторизоваться, и проверить пустит ли с не правильным паролем или нет.
#
import time
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class myTestCase(unittest.TestCase):
    def setUp(self):
        #self.site_url = "https://dev-shop.jowi.club/auth/sign-in"
        self.site_url = 'https://app.jowi.online/auth/sign-in'
        self.inputNomerTelefona = '//input[@name="login"]'
        self.inputPassword = '//input[@name="password"]'
        self.submitVoiti = '//button[contains(text(), "Войти")]'
        self.errMsg_wrongUsrOrPass = '//div[contains(text(), "[20] Неправильный Login или пароль.. ")]'
        self.trueUser = '37455328751'
        self.truePass = 'testtest'
        self.wrongUser = '37455328757'
        self.wrongPass = 'testtest1'
        #
        # FOR WINDOWS
        # #self.driver = webdriver.Firefox()
        # firefox_binary = FirefoxBinary("D:\Programs\Portables\__Browsers\FirefoxPortable_45.0.2\FirefoxPortable.exe")
        # self.driver = webdriver.Firefox(firefox_binary=firefox_binary)
        #
        # FOR LINUX
        path = '/usr/local/bin/geckodriver'
        profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox(executable_path=path, firefox_profile=profile)
        #self.driver.get(self.site_url)
        #print(self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_cases(self):
        print("..... Opening the site "+self.site_url+" .....")
        self.driver.get(self.site_url)
        print("..... Executing Test-Cases .....\n")
        self.tc1('Login via incorrect Phone and incorrect Password')
        self.tc2('Login via incorrect Phone and correct Password')
        self.tc3('Login via correct Phone and incorrect Password')
        self.tc4('Login via correct Phone and correct Password')


    def tc1(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.driver.find_element_by_xpath(self.inputNomerTelefona).clear()
        self.driver.find_element_by_xpath(self.inputPassword).clear()
        self.driver.find_element_by_xpath(self.inputNomerTelefona).send_keys(self.wrongUser)
        self.driver.find_element_by_xpath(self.inputPassword).send_keys(self.wrongPass)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.submitVoiti).click()
        time.sleep(5)
        if self.driver.find_element_by_xpath(self.errMsg_wrongUsrOrPass):
            print("SUCCESS: Can't "+testCaseName)
        else:
            print("ERROR: tc1=>It is possible to "+testCaseName)
        print("----- END TestCase: "+testCaseName+" -----\n")

    def tc2(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.driver.find_element_by_xpath(self.inputNomerTelefona).clear()
        self.driver.find_element_by_xpath(self.inputPassword).clear()
        self.driver.find_element_by_xpath(self.inputNomerTelefona).send_keys(self.wrongUser)
        self.driver.find_element_by_xpath(self.inputPassword).send_keys(self.truePass)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.submitVoiti).click()
        time.sleep(5)
        if self.driver.find_element_by_xpath(self.errMsg_wrongUsrOrPass):
            print("SUCCESS: Can't "+testCaseName)
        else:
            print("ERROR: tc2=>It is possible to "+testCaseName)
        print("----- END TestCase: "+testCaseName+" -----\n")

    def tc3(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.driver.find_element_by_xpath(self.inputNomerTelefona).clear()
        self.driver.find_element_by_xpath(self.inputPassword).clear()
        self.driver.find_element_by_xpath(self.inputNomerTelefona).send_keys(self.trueUser)
        self.driver.find_element_by_xpath(self.inputPassword).send_keys(self.wrongPass)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.submitVoiti).click()
        time.sleep(5)
        if self.driver.find_element_by_xpath(self.errMsg_wrongUsrOrPass):
            print("SUCCESS: Can't "+testCaseName)
        else:
            print("ERROR: tc3=>It is possible to "+testCaseName)
        time.sleep(5)
        print("----- END TestCase: "+testCaseName+" -----\n")

    def tc4(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        loginUrl = self.driver.current_url
        self.driver.find_element_by_xpath(self.inputNomerTelefona).clear()
        self.driver.find_element_by_xpath(self.inputPassword).clear()
        self.driver.find_element_by_xpath(self.inputNomerTelefona).send_keys(self.trueUser)
        self.driver.find_element_by_xpath(self.inputPassword).send_keys(self.truePass)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.submitVoiti).click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        if currentUrl == loginUrl:
            print("ERROR: User hadn't logined")
        else:
            print("SUCCESS: "+testCaseName)
        time.sleep(5)
        print("----- END TestCase: "+testCaseName+" -----\n")

if __name__ == "__main__":
    unittest.main()



    
    
    
    
    
    
    
    
    
    
    