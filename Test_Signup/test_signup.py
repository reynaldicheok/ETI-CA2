#Write Test Case
#Fail Test Case
#Write Enough code to pass test case
#Retest
#Refactor
#Repeat

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Developer's Signup Page Test

#Test Case 1 | View Signup Page
def test_viewSignup():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    results = driver.get('localhost:8000/accounts/signup')
    assert results == 'Signup'
    driver.quit()

#Test Case 2 | Test Empty Parameters
def test_emptyParam():
    driver = webdriver.Chrome()
    Name = ''
    EmailAddr = ''
    Username = ''
    Password = ''
    CfmPassword = ''
    
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    #Click on Signup button
    driver.quit()

#Test Case 3 | Test Valid parameters
def test_validAccount():
    driver = webdriver.Chrome()
    Name = 'kazooie'
    Username = 'kazooie30'
    Password = 'pass123456'
    CfmPassword = 'pass123456'
    
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    #Click on Signup button
    assert results == driver.get('localhost:8000/accounts/login')
    driver.quit()
   
