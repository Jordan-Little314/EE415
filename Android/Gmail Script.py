import os
import unittest
from appium import webdriver

import time

version = input("Enter your platform version: ")
deviceName = input("Enter your device name from ADB: ")

if version == "7.1.1":
    appPackage = 'com.google.android.launcher'
    appActivity = 'com.google.android.launcher.StubApp'
elif version == "4.4.4":
    appPackage = 'com.google.android.launcher'
    appActivity = 'com.google.android.launcher.StubApp'
else:
    appPackage = 'com.google.android.launcher'
    appActivity = 'com.google.android.launcher.StubApp'

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.4.13.1'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = version
desired_caps['deviceName'] = deviceName 
desired_caps['appPackage'] = appPackage
desired_caps['appActivity'] = appActivity

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

wd.implicitly_wait(5)

try:
    while(1):
        if version == "7.1.1":
            print("Loading App... \n")
            time.sleep(1)
            wd.find_element_by_xpath("//android.widget.TextView[@content-desc='Apps']").click()
            time.sleep(1)
            wd.find_element_by_xpath("//android.widget.TextView[@content-desc='Gmail']").click()
            
            #Compose email
            time.sleep(1)
            print("Composing Email...\n")
            wd.find_element_by_id("com.google.android.gm:id/compose_button").click()
            print("Entering:")
            time.sleep(1)
            print("-recipient")
            wd.find_element_by_xpath("//android.widget.MultiAutoCompleteTextView").send_keys("415testacc@gmail.com")
            wd.find_element_by_xpath("//android.widget.MultiAutoCompleteTextView").click()
            print("-subject")
            wd.find_element_by_id("com.google.android.gm:id/subject").send_keys("This is a Test")
            print("-body\n")
            wd.find_element_by_id("com.google.android.gm:id/composearea_tap_trap_bottom").send_keys("Here's a picture of a super cute doggo traveling at incredibly high speed.")
            
            #Attach Picture
            print("Attaching picture...\n")
            wd.find_element_by_id("com.google.android.gm:id/add_attachment").click()
            time.sleep(2)
            wd.find_element_by_xpath("//android.widget.TextView[@text='Attach file']").click()
            
            time.sleep(1)
            wd.find_element_by_id("android:id/title").click()
            time.sleep(2)
            wd.find_element_by_id("com.google.android.gm:id/send").click()
            time.sleep(2)
            print("\nEmail sent successfully!")
            wd.swipe(752,1208,752,263)
            time.sleep(2)
            wd.swipe(752,263,752,1308)
            time.sleep(2)

            wd.tap([(752, 263)])
            time.sleep(4)
            wd.find_element_by_id("com.google.android.gm:id/delete").click()
            
            wd.back()
            wd.back()
            wd.back()

        elif version == "4.4.4":

            print("Loading App... \n")
            time.sleep(1)
            wd.find_element_by_xpath("//android.widget.TextView[@content-desc='Apps']").click()
            time.sleep(1)
            wd.find_element_by_xpath("//android.widget.TextView[@content-desc='Gmail']").click()
            
            #Compose email
            time.sleep(1)
            print("Composing Email...\n")
            wd.find_element_by_id("com.google.android.gm:id/compose").click()
            print("Entering:")
            time.sleep(1)
            print("-recipient")
            wd.find_element_by_xpath("//android.widget.MultiAutoCompleteTextView").send_keys("415testacc@gmail.com")
            wd.find_element_by_xpath("//android.widget.MultiAutoCompleteTextView").click()
            print("-subject")
            wd.find_element_by_id("com.google.android.gm:id/subject").send_keys("This is a Test")
            print("-body\n")
            wd.find_element_by_id("com.google.android.gm:id/body").send_keys("Here's a picture of a super cute doggo traveling at incredibly high speed.")
            
            #Attach Picture
            print("Attaching picture...\n")
            wd.find_element_by_xpath("//android.widget.ImageButton[@content-desc='More options']").click()
            time.sleep(1)
            wd.find_element_by_xpath("//android.widget.TextView[@text='Attach picture']").click()
            time.sleep(1)
            #wd.find_element_by_xpath("//android.widget.TextView[@text='Images']").click()
            #time.sleep(1)
            #wd.find_element_by_xpath("//android.widget.TextView[@text='Camera']").click()
            #time.sleep(1)
            wd.find_element_by_id("com.android.documentsui:id/date").click()
            
            wd.find_element_by_id("com.google.android.gm:id/send").click()
            time.sleep(2)
            print("\nEmail sent successfully!")
            wd.swipe(389,806,389,215)
            time.sleep(2)
            wd.swipe(389,215,389,906)
            time.sleep(2)

            wd.tap([(389,215)])
            time.sleep(4)
            #wd.find_element_by_id("com.google.android.gm:id/delete").click()
            
            wd.back()
            wd.back()
            wd.back()

    else:
        print("Unrecognized version number.")
        
finally:
    wd.quit()
    if not success:
        print('Failure')
