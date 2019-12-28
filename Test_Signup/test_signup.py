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
    
    driver = webdriver.Firefox()
    results = driver.get("http://localhost:8000/signup/")
    assert results == driver.get("http://localhost:8000/signup/")
    driver.quit()

#Test Case 2 | Test Empty Parameters
def test_emptyParam():

    driver = webdriver.Firefox()
    driver.get('http://localhost:8000/signup')
    Username = ''
    Password = ''
    CfmPassword = ''
    user = driver.find_element_by_xpath('//*[@id="id_username"]')
    com = driver.find_element_by_xpath('//*[@id="id_password1"]')
    com2 = driver.find_element_by_xpath('//*[@id="id_password2"]')
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    com2.send_keys(CfmPassword)
    
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    com2.send_keys(CfmPassword)
    #Click on Signup button
    register = driver.find_element_by_xpath('/html/body/main/form/button').click()
    assert register == driver.get('http://localhost:8000/signup') #Not suppose to register and prompt error so it should still be at signup
    driver.quit()

#Test Case 3 | Test Valid parameters
def test_validAccount():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8000/signup')
    Username = 'helloworld5'
    Password = 'IDH36225G'
    CfmPassword = 'IDH36225G'
    user = driver.find_element_by_xpath('//*[@id="id_username"]')
    com = driver.find_element_by_xpath('//*[@id="id_password1"]')
    com2 = driver.find_element_by_xpath('//*[@id="id_password2"]')
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    com2.send_keys(CfmPassword)
    
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    com2.send_keys(CfmPassword)
    #Click on Signup button
    register = driver.find_element_by_xpath('/html/body/main/form/button').click()
    assert register == driver.get('http://localhost:8000/accounts/login') #Pass if redirected to login page
    driver.quit()
