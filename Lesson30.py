from datetime import time
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

id_start = 'startTest'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', id_start)))
button_start = driver.find_element('id', id_start)
button_start.click()
time.sleep(3)

xpath_q1_a1 = '//div[@id="question_0"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q1_a1)))
button_q1_a1 = driver.find_element('xpath',xpath_q1_a1)
button_q1_a1.click()
time.sleep(3)
xpath_q2_a2 = '//div[@id="question_1"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q2_a2)))
button_q2_a2 = driver.find_element('xpath',xpath_q2_a2)
button_q2_a2.click()
time.sleep(3)
xpath_q3_a3 = '//div[@id="question_2"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q3_a3)))
button_q3_a3 = driver.find_element('xpath',xpath_q3_a3)
button_q3_a3.click()
time.sleep(3)
xpath_q4_a4 = '//div[@id="question_3"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q4_a4)))
button_q4_a4 = driver.find_element('xpath',xpath_q4_a4)
button_q4_a4.click()
time.sleep(3)
xpath_q5_a5 = '//div[@id="question_4"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q5_a5)))
button_q5_a5 = driver.find_element('xpath',xpath_q5_a5)
button_q5_a5.click()
time.sleep(3)
xpath_q6_a6 = '//div[@id="question_5"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q6_a6)))
button_q6_a6 = driver.find_element('xpath',xpath_q6_a6)
button_q6_a6.click()
time.sleep(3)
xpath_q7_a7 = '//div[@id="question_6"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q7_a7)))
button_q7_a7 = driver.find_element('xpath',xpath_q7_a7)
button_q7_a7.click()
time.sleep(3)
xpath_q8_a8 = '//div[@id="question_7"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q8_a8)))
button_q8_a8 = driver.find_element('xpath',xpath_q8_a8)
button_q8_a8.click()
time.sleep(3)
xpath_q9_a9 = '//div[@id="question_8"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q9_a9)))
button_q9_a9 = driver.find_element('xpath',xpath_q9_a9)
button_q9_a9.click()
time.sleep(3)
xpath_q10_a10 = '//div[@id="question_9"]//div[@data-answerid="0"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q10_a10)))
button_q10_a10 = driver.find_element('xpath',xpath_q10_a10)
button_q10_a10.click()
time.sleep(3)





# driver = webdriver.Chrome()
# driver.get('https://test.mensa.no/')
# driver.maximize_window()
# xpath_button_18_50 = '//button[contains(@class,"ageselect_1850")]'
# WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_button_18_50)))
# button_18_50 = driver.find_element('xpath', xpath_button_18_50)
# button_18_50.click()
# time.sleep(0.5)
#
# id_start = 'startTest'
# WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', id_start)))
# button_start = driver.find_element('id', id_start)
# button_start.click()
# time.sleep(0.5)
#
# d = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# for number in d:
#     xpath_q_b = f'//div[@id="question_{number}"]//div[@data-answerid="0"]'
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_q_b)))
#     q_b = driver.find_element('xpath', xpath_q_b)
#     q_b.click()
#     time.sleep(0.5)