from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction

import time
import os
import sys

udid = '\0'
device = '\0'

if (len(sys.argv) > 1):
	device = sys.argv[1]
	device.lower()
	if (device == 'iphone'):
		udid = 'db0a6e7a33ffe3790ce2e744f772f098aadcbd19'
	elif (device == 'ipad'):
		udid = '39dd7023db21c794ab18ec38aa4d2aa78bfa20a1'


success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.2'
desired_caps['udid'] = udid
#'db0a6e7a33ffe3790ce2e744f772f098aadcbd19' #iPhone
#'39dd7023db21c794ab18ec38aa4d2aa78bfa20a1' #ipad

desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/WSU/Library/Developer/Xcode/DerivedData/Client-cgmtoaypoecbasgmyjmcqmmhtwkh/Build/Products/Fennec-iphoneos/Client.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	wd.find_element_by_name("IntroViewController.startBrowsingButton").click()
	wd.find_element_by_name("url").click()
	wd.find_element_by_name("url").send_keys("gmail.com", Keys.RETURN)
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]").send_keys("415testacc@gmail.com")
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]").send_keys("ee4152016")
	wd.find_element_by_name("Sign in").click()
	wd.find_element_by_name("SaveLoginPrompt.dontSaveButton").click()
	wd.find_element_by_name("mobile Gmail site").click()
	wd.find_element_by_name("Compose").click()
	wd.find_element_by_name("To:").send_keys("415testacc@gmail.com")
	wd.find_element_by_name("John Smith 415testacc@gmail.com").click()
	wd.find_element_by_name("Subject:").send_keys("Check out this article!")
	wd.find_element_by_name("Done").click()
	wd.find_element_by_name("Message body").click()
	wd.find_element_by_name("Message body").send_keys("I found this article interesting, hopefully you do too!", Keys.RETURN)
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 1.0, "x": 143, "y": 222 })
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 215, "y": 82 })
	wd.find_element_by_name("Done").click()
	wd.find_element_by_name("Cc/Bcc:").click()
	wd.find_element_by_name("Send").click()
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 157, "y": 213 })
	wd.find_element_by_name("Star").click()
	wd.find_element_by_name("TabToolbar.menuButton").click()
	wd.find_element_by_name("NewTabMenuItem").click()

finally:
	#wd.quit()
	if not success:
		raise Exception("Test failed.")
