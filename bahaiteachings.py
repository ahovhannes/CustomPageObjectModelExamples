#
# Author: Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
#
import time
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class myTestCase(unittest.TestCase):
    
    def setUp(self):        
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        #
        self.probel5 = '      '
        self.site_url = 'http://develop.bahaiteachings.org/'
        #
        self.topInfoDiv = '/html/body/div[2]'
        self.gotItBtn = '//a[contains(text(), "GOT IT")]'
        self.iBtn = '/html/body/div[2]/div/div/div[1]/div[1]/a'
        self.headerSearchField = '/html/body/header/div/div/div[2]/div[1]/form/div/input'
        self.headerSearchFieldBtn = '/html/body/header/div/div/div[2]/div[1]/form/div/button'

    def tearDown(self):
        self.driver.close()

    def test_cases(self):
        print("..... Opening the site "+self.site_url+" .....")
        self.driver.get(self.site_url)
        print("..... Executing Test-Cases .....\n")
        #
        #self.clickOnSignInBtn('Check SignIn button existence and click on it')
        ##self.tc1('Login via incorrect Email and incorrect Password')
        ##self.tc2('Login via incorrect Email and correct Password')
        ##self.tc3('Login via correct Email and incorrect Password')
        #self.tc4('Login via correct Email and correct Password')
        ##
        #self.goToMyOrders('Going to MyOrders by clicking on link')
        #self.goToAllProducts('Going to All Products page')
        #self.clickOnProduct('Clicking on Product')
        #self.addChoosedProductToCart('Add choosed product to Cart')
        #self.goToMyAccount('Going to MyAccount')
        #self.goToMyOrders('Going to MyOrders by clicking on link')
        ##
        #self.doLogOut('Doing Sign Out')
        #
        self.headers_GotIt_button("Chechink headers GOT IT button functionality for show/hide top-info section")
        self.headers_Search("CHechink functionality for header's Search")
        

    #Checks element existence by xpath
    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True


    #Chechink headers GOT IT button functionality for show/hide top-info section
    def headers_GotIt_button(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.headers_GotIt_button_close(self.probel5+"Clicking on headers GOT IT button to hide top-info section")
        self.headers_GotIt_button_open(self.probel5+ "Clicking on headers 'i' button to show top-info section")
        print("----- END TestCase: "+testCaseName+" -----\n")

    #Clicking on headers GOT IT button to hide top-info section
    def headers_GotIt_button_close(self, testCaseName):        
        topInfoDiv_class = self.driver.find_element_by_xpath(self.topInfoDiv).get_attribute("class") #top-info
        #print("***topInfoDiv_class="+str(topInfoDiv_class))
        self.driver.find_element_by_xpath(self.gotItBtn).click()
        topInfoDiv_class_afterClose = self.driver.find_element_by_xpath(self.topInfoDiv).get_attribute("class") #top-info _closed
        #print("***topInfoDiv_class_afterClose="+str(topInfoDiv_class_afterClose))
        assert topInfoDiv_class != topInfoDiv_class_afterClose, "ERROR: top-info section there wern't closed after the click on GOT IT button"
        print(testCaseName+" --> SUCCESS")
        time.sleep(2)

    #Clicking on headers 'i' button to show top-info section
    def headers_GotIt_button_open(self, testCaseName):
        topInfoDiv_class = self.driver.find_element_by_xpath(self.topInfoDiv).get_attribute("class") #top-info _closed
        self.driver.find_element_by_xpath(self.iBtn).click()
        topInfoDiv_class_afterClose = self.driver.find_element_by_xpath(self.topInfoDiv).get_attribute("class") #top-info
        assert topInfoDiv_class != topInfoDiv_class_afterClose, "ERROR: top-info section there wern't closed after the click on GOT IT button"
        print(testCaseName+" --> SUCCESS")
        time.sleep(2)


    #CHechink functionality for header's Search
    def headers_Search(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        #Do searching for existing word
        serchingWord = 'Maya'
        if self.are_there_element_in_page_after_Search(serchingWord):
            print(self.probel5+"SUCCESS: The existing word '"+serchingWord+"' were find into the page")
        else:
            print(self.probel5+"ERROR: The existing word '"+serchingWord+"' there weren't find into the page")
        #Do searching for non existing word
        serchingWord = 'Maya7'
        if not self.are_there_element_in_page_after_Search(serchingWord):
            print(self.probel5+"SUCCESS: Not existing word '"+serchingWord+"' there weren't find into the page")
        else:
            print(self.probel5+"ERROR: Not existing word '"+serchingWord+"' were find into the page")

        print("----- END TestCase: "+testCaseName+" -----\n")
        #time.sleep(2)

    #Are there element in page after Search
    def are_there_element_in_page_after_Search(self, serchingWord):
        #serchingWord = 'Maya'        
        findedWordsXpath = "//*[contains(text(), "+serchingWord+")]"
        noResults = '//div[@class="no-results not-found"]'
        pageHasResults = '//div[@class="posts flex-btw"]'        
        #Do Searching
        self.driver.find_element_by_xpath(self.headerSearchField).clear()
        self.driver.find_element_by_xpath(self.headerSearchField).send_keys(serchingWord)
        self.driver.find_element_by_xpath(self.headerSearchFieldBtn).click()
        #Checking searched world existence into the page
        if self.check_exists_by_xpath(noResults):
            return False
        elif self.check_exists_by_xpath(pageHasResults):
            if self.check_exists_by_xpath(findedWordsXpath):
                return True
            else:
                print(self.probel5+"ERROR: Bad case ...")
                return False
        else:
            print(self.probel5+"ERROR: Wrong case ...")
            return False


    #Doing click action on SignIn button
    def clickSignInBtn(self):
        self.driver.find_element_by_xpath(self.headerLoginBtn).click()

    #Check SignIn button existence and click on it
    def clickOnSignInBtn(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        if self.check_exists_by_xpath(self.headerLoginBtn):
            print(self.probel5+"SUCCESS: SignIn button presented on page")
            #self.driver.find_element_by_xpath(self.headerLoginBtn).click()
            self.clickSignInBtn()
        else:
            print(self.probel5+"ERROR: SignIn button "+str(self.headerLoginBtn)+" doesn't exists")
        print("----- END TestCase: "+testCaseName+" -----\n")

    #Inputs Email, inputs Password and clicks on SignIn button
    def doLogin(self, login, password):
        self.driver.find_element_by_xpath(self.inputEmail).clear()
        self.driver.find_element_by_xpath(self.inputPassword).clear()
        self.driver.find_element_by_xpath(self.inputEmail).send_keys(login)
        self.driver.find_element_by_xpath(self.inputPassword).send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.submitVoiti).click()

    #Do LogOut
    def doLogOut(self, testCaseName):
        print("..... Doing Sign Out .....")
        loginButtonElement = self.wait.until(lambda driver: driver.find_element_by_xpath(self.myAccountIcon))
        loginButtonElement = self.wait.until(lambda driver: driver.find_element_by_xpath(self.myAccountHoverLogOut))
        time.sleep(5)


    #Login via incorrect Email and incorrect Password
    def tc1(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.doLogin(self.wrongUser, self.wrongPass)
        #time.sleep(5)
        currentUrl = self.driver.current_url
        if currentUrl == self.loginUrl:
            print(self.probel5+"SUCCESS: Can't "+testCaseName)
        else:
            print(self.probel5+"ERROR: tc1=>It is possible to "+testCaseName)
        print("----- END TestCase: "+testCaseName+" -----\n")

    #Login via incorrect Email and correct Password
    def tc2(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.doLogin(self.wrongUser, self.truePass)
        time.sleep(5)
        currentUrl = self.driver.current_url
        if currentUrl == self.loginUrl:
            print(self.probel5+"SUCCESS: Can't "+testCaseName)
        else:
            print(self.probel5+"ERROR: tc2=>It is possible to "+testCaseName)
        print("----- END TestCase: "+testCaseName+" -----\n")

    #Login via correct Email and incorrect Password
    def tc3(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.doLogin(self.trueUser, self.wrongPass)
        time.sleep(5)
        currentUrl = self.driver.current_url
        if currentUrl == self.loginUrl:
            print(self.probel5+"SUCCESS: Can't "+testCaseName)
        else:
            print(self.probel5+"ERROR: tc3=>It is possible to "+testCaseName)
        print("----- END TestCase: "+testCaseName+" -----\n")

    #Login via correct Email and correct Password
    def tc4(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        self.doLogin(self.trueUser, self.truePass)
        currentUrl = self.driver.current_url
        if currentUrl == self.loginUrl:
            print(self.probel5+"ERROR: User hadn't logined")
        else:
            print(self.probel5+"SUCCESS: "+testCaseName)
        time.sleep(5)
        print("----- END TestCase: "+testCaseName+" -----\n")

    #Going to My Orders
    def goToMyOrders(self, testCaseName):
        print("..... "+testCaseName+" .....")
        self.driver.find_element_by_xpath(self.myOrdersLink).click()
        time.sleep(2)

    #Going to All Products page
    def goToAllProducts(self, testCaseName):
        print("..... "+testCaseName+" .....")
        self.driver.find_element_by_xpath(self.allProductsLink).click()
        time.sleep(2)

    #Click on Product
    def clickOnProduct(self, testCaseName):
        print("..... "+testCaseName+" .....")
        self.driver.find_element_by_xpath(self.productFromAllProducts).click()
        time.sleep(5)

    #Add choosed product to Cart
    def addChoosedProductToCart(self, testCaseName):
        print("..... "+testCaseName+" .....")
        #Choosing Color
        self.driver.find_element_by_xpath(self.choosedProductColor).click()
        #Choosing Size
        self.driver.find_element_by_xpath(self.choosedProductSize).click()
        #Choosing Quantity
        self.driver.find_element_by_xpath(self.choosedProductQuantity).click()
        time.sleep(2)
        #Click on ADD TO CART
        self.driver.find_element_by_xpath(self.choosedProductAddToCartBtn).click()
        #Close after AddToCart pop-up
        popupCloseIcon = '/html/body/div[2]/div/div[1]/div[2]/button'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, popupCloseIcon))).click()
        #
        #alert_obj = self.driver.switch_to.alert
        #alert_obj.dismiss()
        time.sleep(5)

    #Going to MyAccount
    def goToMyAccount(self, testCaseName):        
        but_loc = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.myAccountIcon)))#hover over button
        ActionChains(self.driver).move_to_element(but_loc).perform()
        sec_but = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.myAccountHoverMyAccount))) #click on contact
        sec_but.click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()





