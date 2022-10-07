
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#https://www.selenium.dev/documentation/webdriver/waits/
driver = webdriver.Chrome()
driver.get('https://test.mensa.no/')
# driver.maximize_window()


xpath_button_18_50 = '//button[contains(@class,"ageselect_1850")]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_button_18_50)))
button_18_50 = driver.find_element('xpath',xpath_button_18_50)
button_18_50.click()
