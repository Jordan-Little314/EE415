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
    time.sleep(8)
    #The first back button is for the advertisement
    wd.back()
    time.sleep(1)
    #The second back button is for getting to the home screen
    wd.back()

    #Facebook section
    wd.find_element_by_name("Facebook").click()

    #This script scrolls through the main screen until it sees something to like, then it likes it.
    like_flag = 1
    while (like_flag):
        try:
            wd.find_element_by_name("Like").click()
            like_flag = 0
        except:
            wd.swipe(500, 1900, 500, 1300) #(x-cord, y-cord, x-finalcord, y-finalcord, 1(optional duration)

    #swipe to the top of the screen
    time.sleep(2)
    wd.swipe(500, 500, 500, 1900)
    time.sleep(1)
    wd.swipe(500, 500, 500, 1900)
    time.sleep(1)
    wd.swipe(500, 500, 500, 1900)
    time.sleep(1)
    #write a facebook post
    wd.tap([(400, 900)])
    wd.implicitly_wait(5)
    wd.find_element_by_id("com.facebook.katana:id/composer_status_text").send_keys("This is a facebook post.")
    wd.implicitly_wait(5)
    wd.find_element_by_id("com.facebook.katana:id/primary_named_button").click()
    wd.back()

    #Google maps script
    wd.implicitly_wait(5)
    wd.find_element_by_name("Maps").click()
    time.sleep(5)
    wd.implicitly_wait(5)
    #search for PNNL
    wd.tap([(500, 150)])
    wd.find_element_by_id("com.google.android.apps.maps:id/search_omnibox_edit_text").send_keys("Pacific Northwest National Laboratory")
    time.sleep(3)
    wd.tap([(1100, 500)])
    #look for directions
    time.sleep(5)
    wd.tap([(1300, 2200)])

    time.sleep(2)
    wd.back()
    time.sleep(1)
    wd.back()
    time.sleep(1)
    wd.back()

    #gmail script
    wd.implicitly_wait(5)
    wd.find_element_by_name("Gmail").click()
    wd.implicitly_wait(5)
    wd.find_element_by_id("com.google.android.gm:id/compose_button").click()
    wd.implicitly_wait(5)
    wd.find_element_by_id("com.google.android.gm:id/to").send_keys("415testacc@gmail.com")
    wd.implicitly_wait(5)
    wd.tap([(1400,2250)])
    wd.find_element_by_id("com.google.android.gm:id/subject").send_keys("This is the subject")
    wd.tap([(1400,2250)])
    wd.implicitly_wait(5)
#    wd.find_element_by_id("com.google.android.gm:id/body").send_keys("This is the body of the email")
    wd.find_element_by_xpath("//android.webkit.WebView[@index='0']").send_keys("This is the body of the email")
    wd.implicitly_wait(5)
    wd.find_element_by_id("com.google.android.gm:id/send").click()
    wd.back()
finally:
    wd.quit()
    if not success:
        print('Failure')
