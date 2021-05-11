from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from DBlocation import *
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
print("hi")
def AutoLogin(Service,LoginId,password):
    if(loc(Service)):
        website,signin,emailidp,passwordp,signinb=loc(Service)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(website)
        time.sleep(3)

        signIn = driver.find_element_by_xpath(signin).click()
        time.sleep(4)
        emailId = driver.find_element_by_xpath(emailidp)
        emailId.send_keys(LoginId)   
        passwordInput = driver.find_element_by_xpath(passwordp)
        passwordInput.send_keys(password)
        signInButton = driver.find_element_by_xpath(signinb).click()
        return True
    else:
        return False
AutoLogin('DISNEY+',"bruh","bruh123")