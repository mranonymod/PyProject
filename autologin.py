from selenium import webdriver
import time
from creds import LoginId,password
from location import signin,website,emailidp,passwordp,signinb

driver = webdriver.Chrome()
driver.get(website)
time.sleep(3)

signIn = driver.find_element_by_xpath(signin).click()
time.sleep(4)
emailId = driver.find_element_by_xpath(emailidp)
emailId.send_keys(LoginId)   
passwordInput = driver.find_element_by_xpath(passwordp)
passwordInput.send_keys(password)
signInButton = driver.find_element_by_xpath(signinb).click()