#Write Test Case
#Fail Test Case
#Write Enough code to pass test case
#Retest
#Refactor
#Repeat
from django.test import LiveServerTestCase, TestCase, Client
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Developer's Todo Page Unit Test
executable_path=r'C:\Users\Reynaldi\Documents\ETI-CA2\chromedriver.exe'
def setUp(self):    
    print('Setup')
    self.unauth_client = Client()
    self.auth_client = Client()
    self.auth_client.login(username='Reynaldi',password='123456789')

        
#Test Case 1 | View Todo Page with no login
def test_viewTodo():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    #driver = webdriver.Chrome(options=op)
    
    driver = webdriver.Chrome(executable_path)
    driver.get('localhost:8000/todo')
    time.sleep(3)
    assert driver.title == "Login"
    driver.quit()

#Test Case 2 | View Todo Page with login
def test_viewTodoLogin():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(executable_path)
    driver.get('localhost:8000/accounts/login')
    Username = 'Reynaldi'
    Password = '123456789'
    user = driver.find_element_by_name('username')
    time.sleep(2)
    com = driver.find_element_by_name('password')
    user.send_keys(Username)
    com.send_keys(Password)
    #driver.find_element_by_id("LoginBtn").click()
    login = driver.find_element_by_xpath('//*[@id="LoginBtn"]').click()
    time.sleep(5)
    assert driver.title == "To Do Page"
    driver.quit()
    
    
    
#Test Case 3 Test if the add function works
def test_addtoDo():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(executable_path)
    driver.get('localhost:8000/accounts/login')
    Username = 'Reynaldi'
    Password = '123456789'
    user = driver.find_element_by_name('username')
    time.sleep(2)
    com = driver.find_element_by_name('password')
    user.send_keys(Username)
    com.send_keys(Password)
    driver.find_element_by_id("LoginBtn").click()
    #driver.find_element_by_name('content').send_keys('Testingx')
    #time.sleep(2)
    #driver.find_element_by_name('Adding').click()
    #time.sleep(2)
    time.sleep(1)
    #login = driver.find_element_by_xpath('//*[@id="LoginBtn"]').click()
    inputtxt = driver.find_element_by_xpath('/html/body/main/form/input[2]')
    inputtxt.send_keys('Testx1')
    addbtn = driver.find_element_by_xpath('/html/body/main/form/input[3]').click()
    time.sleep(5)
    assert driver.title == "To Do Page"
    driver.quit()
    
#Test Case 4 Test if the delete function works
def test_deltoDo():
    driver = webdriver.Chrome(executable_path)
    driver.get('localhost:8000/accounts/login')
    driver.find_element_by_name('username').send_keys('Reynaldi')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('123456789')
    time.sleep(1)
    driver.find_element_by_id("LoginBtn").click()
    time.sleep(1)
    driver.find_element_by_name('deleting').click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(6)
    
    assert driver.title == "To Do Page"
    driver.quit()

#Test Case 5 Test if the history page button works
def test_HistoryToDo():
    driver = webdriver.Chrome(executable_path)
    driver.get('localhost:8000/accounts/login')
    driver.find_element_by_name('username').send_keys('Reynaldi')
    time.sleep(2)
    driver.find_element_by_name('password').send_keys('123456789')
    time.sleep(2)
    driver.find_element_by_id("LoginBtn").click()
    time.sleep(2)
    driver.find_element_by_name('hist').click()
    time.sleep(2)
    time.sleep(7)
    
    assert driver.title == "To Do Page History"
    driver.quit()

