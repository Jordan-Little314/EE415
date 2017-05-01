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
desired_caps['appPackage'] = 'free.vpn.unblock.proxy.turbovpn'
desired_caps['appActivity'] = 'free.vpn.unblock.proxy.turbovpn.activity.VpnMainActivity'

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wd.implicitly_wait(5)

try:
#    wd.implicitly_wait(5)
    time.sleep(10)
    #run the vpn after waiting for the initial ad
    wd.find_element_by_id("free.vpn.unblock.proxy.turbovpn:id/connectImageView").click()
    #This is a little weird, and inconsistent. It seems the first time you
    #load the application and want to run the vpn, it asks you to confirm,
    #but in subsequent runs through the application, this confirmation disappears.
    #I need to figure out a way to have it accept if this message shows up,
    #and properly continue if the message isn't seen. Perhaps another try statement?
    #wd.find_element_by_id("android:id/button1").click() #accept

    #This sleep is so the back button isn't pressed until the vpn is up
    time.sleep(10)
    #The first back button is for the advertisement
    wd.back()
    time.sleep(1)
    #The second back button is for getting to the home screen
    wd.back()
    #This opens the facebook application assuming it is on the same page as
    #your vpn application. Might need to modify if you have many apps
    wd.find_element_by_name("Facebook").click()

    #From here you can add any standard facebook script.
    #One note: Because we are pressing the facebook button instead of loading
    #into a specific activity, the activity will not always be the same.
    #You may want to clear all running applications before running this script
    #to keep it consistent.

    #This script scrolls through the main screen until it sees something to like, then it likes it.
    like_flag = 1
    while (like_flag):
        try:
            wd.find_element_by_name("Like").click()
            like_flag = 0
        except:
            wd.swipe(500, 1900, 500, 1400) #(x-cord, y-cord, x-finalcord, y-finalcord, 1(optional duration)
        
finally:
    wd.quit()
    if not success:
        print('Failure')
