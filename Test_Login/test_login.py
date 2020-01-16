#Write Test Case#
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

#Developer's Login Page Unit Test

#Test Case 1 | View Login Page
def test_viewLogin():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    results = driver.get('localhost:8000/accounts/login')
    assert results == 'Login'
    driver.quit()

#Test Case 2 | Test Empty fields
def test_emptyFields():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    Username = ''
    Password = ''
    user = driver.find_element_by_xpath('//*[@id="id_username"]')
    com = driver.find_element_by_xpath('//*[@id="id_password"]')
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    #Click on Login button
    login = driver.find_element_by_xpath('//*[@id="LoginBtn"]').click()
    assert login == driver.get('localhost:8000/accounts/login')
    driver.quit()

#Test Case 3 | Test Valid account
def test_validAccount():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    Username = 'kazooie30'
    Password = '123456789'
    user = driver.find_element_by_xpath('//*[@id="id_username"]')
    com = driver.find_element_by_xpath('//*[@id="id_password"]')
    #Send text into input
    user.send_keys(Username)
    com.send_keys(Password)
    #Click on Login button
    login = driver.find_element_by_xpath('//*[@id="LoginBtn"]').click()
    assert login == driver.get('localhost:8000/todo')
    driver.quit()
