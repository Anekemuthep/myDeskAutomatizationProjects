from selenium import webdriver
from selenium.webdriver.chrome.service import Service
##from selenium.webdriver.common.by import By
##from selenium.webdriver.common.keys import Keys
import time

# http://sites.google.com/chromium.org/driver/

#service = Service(executable_path="chromedriver.exe")
#driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(executable_path="chromedriver.exe")

#driver.get("http://goolge.com")

##input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
##input_element.send_keys("tech with tim" + Keys.ENTER)

#time.sleep(10)

driver.quit()