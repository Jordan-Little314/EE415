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
phone = True

if (len(sys.argv) > 1):
	device = sys.argv[1]
	device.lower()
	if (device == 'iphone'):
		udid = 'db0a6e7a33ffe3790ce2e744f772f098aadcbd19'
	elif (device == 'ipad'):
		udid = '39dd7023db21c794ab18ec38aa4d2aa78bfa20a1'

if (device == 'ipad'):
    phone = False

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
    ##### News

    wd.find_element_by_name("IntroViewController.startBrowsingButton").click()
    wd.find_element_by_name("url").click()
    wd.find_element_by_name("url").send_keys("theguardian.com", Keys.RETURN)

    if (phone):
        wd.find_element_by_name("US politics /").click()
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 106, "y": 205 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 2, "x": 137, "y": 42 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 120, "y": 46 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 120, "y": 43 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 122, "y": 43 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 132, "y": 86 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 112, "y": 90 })
        wd.find_element_by_name("Cancel").click()
        wd.find_element_by_name("TabToolbar.menuButton").click()
        wd.find_element_by_name("NewTabMenuItem").click()
    else:
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]/XCUIElementTypeOther[8]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]").click()
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 111, "y": 473 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 353, "y": 81 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 322, "y": 85 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 326, "y": 86 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 336, "y": 84 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 336, "y": 130 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 244, "y": 134 })
        wd.find_element_by_name("New Tab").click()


    ##### Email

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
    if (phone):
        wd.find_element_by_name("Done").click()
    wd.find_element_by_name("Message body").click()
    wd.find_element_by_name("Message body").send_keys("I found this article interesting, hopefully you do too!", Keys.RETURN)
    if (phone):
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 1.0, "x": 143, "y": 222 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 215, "y": 82 })
        wd.find_element_by_name("Done").click()
        wd.find_element_by_name("Cc/Bcc:").click()
    else:
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 284, "y": 453 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 220, "y": 337 })
    wd.find_element_by_name("Send").click()
    if (phone):
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 157, "y": 213 })
        wd.find_element_by_name("Star").click()
        wd.find_element_by_name("TabToolbar.menuButton").click()
        wd.find_element_by_name("NewTabMenuItem").click()
    else:
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 143, "y": 265 })
        wd.find_element_by_name("New Tab").click()


    ##### Facebook

    wd.find_element_by_name("url").click()
    wd.find_element_by_name("url").send_keys("m.facebook.com", Keys.RETURN)
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
    if (phone):
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 248, "y": 174 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 232, "y": 109 })
    else:
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 495, "y": 238 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 308, "y": 189 })
    wd.find_element_by_name("What's on your mind?").send_keys(Keys.RETURN, time.strftime('%Y-%m-%dT%H:%M:%SZ', timetup))
    wd.find_element_by_name("Post").click()
    if (phone):
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[5]/XCUIElementTypeSwitch[1]").click()
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[6]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]").click()
        wd.find_element_by_name("Write a comment...").send_keys("Hmm... Very interesting interaction. ")
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 62, "y": 557 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 27, "y": 358 })
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]/XCUIElementTypeOther[6]/XCUIElementTypeButton[1]").click()
        wd.find_element_by_name("Done").click()
        wd.find_element_by_name("URLBarView.tabsButton").click()
        wd.find_element_by_name("TabTrayController.menuButton").click()
        wd.find_element_by_name("CloseAllTabsMenuItem").click()
    else:
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[5]/XCUIElementTypeSwitch[1]").click()
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[10]/XCUIElementTypeStaticText[1]").send_keys("Hmm... Very interesting interaction. ")
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 101, "y": 992 })
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 40, "y": 778 })
        wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[6]/XCUIElementTypeOther[12]/XCUIElementTypeButton[1]").click()
        wd.find_element_by_name("TopTabsViewController.tabsButton").click()
        wd.find_element_by_name("TabTrayController.menuButton").click()
        wd.find_element_by_name("CloseAllTabsMenuItem").click()

finally:
	#wd.quit()
	if not success:
		raise Exception("Test failed.")
