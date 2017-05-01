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
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'ZX1G324FVL'
desired_caps['appPackage'] = 'com.facebook.katana'
desired_caps['appActivity'] = 'com.facebook.katana.LoginActivity'

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#was http://0.0.0.0:4723/wd/hub
wd.implicitly_wait(5)

try:
    #Click on status button
    wd.find_element_by_id("com.facebook.katana:id/feed_composer_status_button").click()
    #Write a status.
    wd.find_element_by_id("com.facebook.katana:id/composer_status_text").send_keys("This is a facebook post.")
    wd.implicitly_wait(5)
    #Post the status
    wd.find_element_by_id("com.facebook.katana:id/primary_named_button").click()
    wd.implicitly_wait(5)
        
finally:
    wd.quit()
    if not success:
        print('Failure')
