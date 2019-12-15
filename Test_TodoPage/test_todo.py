#Write Test Case
#Fail Test Case
#Write Enough code to pass test case
#Retest
#Refactor
#Repeat
from django.test import LiveServerTestCase
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Developer's Login Page Unit Test

#Test Case 1 | View Todo Page with no login
def test_viewTodo():
    #op = webdriver.ChromeOptions()
    #op.add_argument('headless')
    #driver = webdriver.Chrome(options=op)
    driver = webdriver.Chrome()
    driver.get('localhost:8000/todo')
    
    assert driver.title == "Login"

#Test Case 2 | View Todo Page with login
def test_viewTodoLogin():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/accounts/login')
    driver.find_element_by_name('username').send_keys('Reynaldi')
    time.sleep(2)
    driver.find_element_by_name('password').send_keys('123456789')
    time.sleep(2)
    driver.find_element_by_id("LoginBtn").click()
    time.sleep(1)
    driver.get('localhost:8000/todo')
    assert driver.title == "To Do Page"
    
    
    
#Test Case 3 Test if the add function works
def test_addtoDo():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/accounts/login')
    driver.find_element_by_name('username').send_keys('Reynaldi')
    time.sleep(2)
    driver.find_element_by_name('password').send_keys('123456789')
    time.sleep(2)
    driver.find_element_by_id("LoginBtn").click()
    driver.find_element_by_name('content').send_keys('Testing')
    time.sleep(2)
    driver.find_element_by_name('Adding').click()
    time.sleep(2)
    time.sleep(1)
    
    assert driver.title == "To Do Page"
#Test Case 4 Test if the delete function works
def test_deltoDo():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/accounts/login')
    driver.find_element_by_name('username').send_keys('Reynaldi')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('123456789')
    time.sleep(1)
    driver.find_element_by_id("LoginBtn").click()
    time.sleep(1)
    driver.find_element_by_name('deleting').click()
    time.sleep(1)
  
    
    assert driver.title == "To Do Page"

#Test Case 5 Test if the history page button works
def test_HistoryToDo():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/accounts/login')
    driver.find_element_by_name('username').send_keys('Reynaldi')
    time.sleep(2)
    driver.find_element_by_name('password').send_keys('123456789')
    time.sleep(2)
    driver.find_element_by_id("LoginBtn").click()
    time.sleep(2)
    driver.find_element_by_name('hist').click()
    time.sleep(2)
    
    
    assert driver.title == "To Do Page History"
