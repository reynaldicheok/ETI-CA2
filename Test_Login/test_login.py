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

#Developer's Login Page Unit Test

#Test Case 1 | View Login Page
def test_viewLogin():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    results = driver.get('localhost:8000/login')
    assert results == "Login"
#Test Case 2
#Test Case 3
#Test Case 4
