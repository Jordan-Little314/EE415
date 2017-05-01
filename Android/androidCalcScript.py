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
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wd.implicitly_wait(5)

try:
    wd.implicitly_wait(5)
    wd.find_element_by_id("com.android.calculator2:id/digit_7").click() #press 7
    wd.tap([(1200, 1600)]) #press *
    wd.find_element_by_name("2").click() #press 2
    wd.find_element_by_xpath("//android.widget.Button[@text='=']").click() #press =

    result = wd.find_element_by_id("com.android.calculator2:id/formula").text #get result
    print('The result was %s' % result)
finally:
    wd.quit()
    if not success:
        print('Failure')
