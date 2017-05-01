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
#'39dd7023db21c794ab18ec38aa4d2aa78bfa20a1' #iPad
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/WSU/Library/Developer/Xcode/DerivedData/Client-cgmtoaypoecbasgmyjmcqmmhtwkh/Build/Products/Fennec-iphoneos/Client.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

timetup = time.gmtime()

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	wd.find_element_by_name("IntroViewController.startBrowsingButton").click()
	wd.find_element_by_name("url").click()
	wd.find_element_by_name("url").send_keys("facebook.com", Keys.RETURN)
	#wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeTextField[1]").send_keys("415testacc@gmail.com")
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeSecureTextField[1]").send_keys("ee4152016!")
	wd.find_element_by_name("Log In").click()
	wd.find_element_by_name("Not Now").click()
	#wd.find_element_by_name("Next").click()
	#wd.find_element_by_name("Next").click()
	#wd.find_element_by_name("Next").click()
	#wd.find_element_by_name("Next").click()

	wd.find_element_by_name("What's on your mind?").send_keys("Check out this awesome article! ")
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 248, "y": 174 })
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 232, "y": 109 })
	wd.find_element_by_name("What's on your mind?").send_keys(Keys.RETURN, time.strftime('%Y-%m-%dT%H:%M:%SZ', timetup))
	wd.find_element_by_name("Post").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[5]/XCUIElementTypeSwitch[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[6]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]").click()
	wd.find_element_by_name("Write a comment...").send_keys("Hmm... Very interesting interaction.")
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 62, "y": 557 })
	wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 27, "y": 358 })
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]/XCUIElementTypeOther[6]/XCUIElementTypeButton[1]").click()
	wd.find_element_by_name("Done").click()
	wd.find_element_by_name("URLBarView.tabsButton").click()
	wd.find_element_by_name("TabTrayController.menuButton").click()
	wd.find_element_by_name("CloseAllTabsMenuItem").click()

finally:
	#wd.quit()
	if not success:
		raise Exception("Test failed.")
