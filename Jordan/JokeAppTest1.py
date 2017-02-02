from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.2'
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/WSU/Library/Developer/Xcode/DerivedData/Homework_2_(Joke_App)-axpklxluqpqqsjfvojodtotpwlum/Build/Products/Release-iphonesimulator/Homework 2 (Joke App).app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	wd.find_element_by_name("New Joke").click()
	wd.find_element_by_name("Answer").click()
	wd.find_element_by_name("New Joke").click()
finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")
