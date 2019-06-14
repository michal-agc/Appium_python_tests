import unittest
import os
from appium import webdriver 
import time
from selenium import webdriver as swd

#class AndroidTests(unittest.TestCase):

    #def setUp(self):

desired_caps = {'deviceName': 'Android',
                        'platformName': 'Android',
                        'appPackage': 'com.busmancard',
                        'appActivity': '.MainActivity',
                        'automationName': 'UiAutomator2'}
  
os.system("appium")
   
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10000)


        
emailField = driver.find_elements_by_class_name("android.widget.EditText")[0]
passField = driver.find_elements_by_class_name("android.widget.EditText")[1]
passConfirmField = driver.find_elements_by_class_name("android.widget.EditText")[2]        
loginButton = driver.find_elements_by_class_name("android.widget.TextView")[1]
applyButton = driver.find_elements_by_class_name("android.widget.TextView")[2]

loginButton.click()
time.sleep(2)

emailField2 = driver.find_elements_by_class_name("android.widget.EditText")[0]
passField2 = driver.find_elements_by_class_name("android.widget.EditText")[1]
applyButton2 = driver.find_elements_by_class_name("android.widget.TextView")[1]


emailField2.send_keys("test@test.pl")
passField2.send_keys("Password123")
applyButton2.click()
for i in range(4):
    el = driver.find_elements_by_class_name("android.widget.ImageView")[i]
    el.click()
    time.sleep(2)
    
el = driver.find_elements_by_class_name("android.widget.ImageView")[0]
el.click()
time.sleep(2)
actions = webdriver.common.touch_action.TouchAction(driver)
actions.tap(None,446,432)
actions.perform()

browser = swd.Firefox()
browser.get("http://18.195.158.221:4000/#/login")
browser.find_element_by_xpath("//*[@id=\"username\"]").send_keys("admin@agc.pl")
browser.find_element_by_xpath("//*[@id=\"password\"]").send_keys("admin")
browser.find_element_by_xpath("/html/body/div/div/div/form/div[2]/button").click()
time.sleep(2)
browser.find_element_by_xpath("/html/body/div/div/div/div/main/div[1]/div/div/a[4]").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/main/div[2]/div/div/div[2]/table/tbody/tr[2]/td[3]").click()





#emailField.send_keys("test@test.pl")
#passField.send_keys("Password123")
#passConfirmField.send_keys("Password123")
        

#applyButton.click()

#os.system("appium --address 127.0.0.1 --port 4723 --session-override") 
