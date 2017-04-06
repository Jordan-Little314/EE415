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
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/WSU/Library/Developer/Xcode/DerivedData/Client-cgmtoaypoecbasgmyjmcqmmhtwkh/Build/Products/Fennec-iphonesimulator/Client.app')
#/Users/WSU/Library/Developer/Xcode/DerivedData/Client-elgfethedbgmomhgdohowwlruvgz/Build/Products/Fennec-iphonesimulator/Client.app

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

touchAction = TouchAction(wd)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	wd.find_element_by_name("URLBarView.tabsButton").click()
	wd.find_element_by_name("TabTrayController.menuButton").click()
	wd.find_element_by_name("CloseAllTabsMenuItem").click()
	wd.find_element_by_name("url").click()
	wd.find_element_by_name("url").send_keys("www.bbc.com", Keys.RETURN)
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[8]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeLink[1]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]").click()
	#touchAction.long_press(wd.find_element_by_name("url"), 1000).release().perform()

	wd.find_element_by_name("TabToolbar.menuButton").click()
	wd.find_element_by_name("NewTabMenuItem").click()
	wd.find_element_by_name("url").send_keys("gmail.com", Keys.RETURN)
	wd.find_element_by_name("Compose").click()
	wd.find_element_by_name("To:").send_keys("415testacc@gmail.com")
	wd.find_element_by_name("Subject:").send_keys("Check out this news article!")
	wd.find_element_by_name("Message body").send_keys("This article is really interesting! [insert article] Thought you would enjoy it!")
	wd.find_element_by_name("Send").click()


finally:
	#wd.quit()
	if not success:
		raise Exception("Test failed.")
