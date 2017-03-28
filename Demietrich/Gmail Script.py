#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.common.action_chains import ActionChains

import os
import unittest
from appium import webdriver

import time

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.4.13.1'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'HT4CSJT02356' 
desired_caps['appPackage'] = 'com.google.android.gm'
desired_caps['appActivity'] = 'com.google.android.gm.GmailActivity'

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#was http://0.0.0.0:4723/wd/hub
wd.implicitly_wait(5)

try:
    #Compose email
    wd.find_element_by_id("com.google.android.gm:id/compose").click()
    wd.find_element_by_xpath("//android.widget.MultiAutoCompleteTextView").send_keys("415testacc@gmail.com")
    wd.find_element_by_id("com.google.android.gm:id/subject").send_keys("This is a Test")
    wd.find_element_by_id("com.google.android.gm:id/body").send_keys("Body of the email goes here.")
    
    #Attach Picture
    wd.find_element_by_xpath("//android.widget.ImageButton").click()
    wd.find_element_by_name("Attach picture").click()
    wd.find_element_by_id("com.android.documentsui:id/icon_thumb").click()
    wd.find_element_by_id("com.google.android.gm:id/send").click()
    wd.implicitly_wait(5)

    wd.navigate().back()
        
finally:
    wd.quit()
    if not success:
        print('Failure')
