from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction



import time
import os

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.3'
desired_caps['deviceName'] = 'iPad'
desired_caps['app'] = os.path.abspath('/Users/WSU/Library/Developer/Xcode/DerivedData/JokerBarBuddy-docwtcejxwqahybpjzfgwkgetihf/Build/Products/Debug-iphoneos/JokerBarBuddy.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	wd.find_element_by_name("Find Bar").click()
	wd.find_element_by_name("Show Nearby Bars").click()
	wd.find_element_by_name("Main").click()
	wd.find_element_by_name("Get Joke").click()
finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")
