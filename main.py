import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/racool/Desktop/chromedriver'
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3223387506&f_AL=true&geoId'
           '=104233796&keywords=customer%20service&location=St%20John%E2%80%99s%2C%20Newfoundland%20and%20Labrador%2C'
           '%20Canada&refresh=true')
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
driver.find_element(By.ID, 'username').send_keys(username)
p = driver.find_element(By.ID, 'password')
p.send_keys(password)
p.send_keys(Keys.RETURN)
driver.find_element(By.CLASS_NAME, 'jobs-s-apply').click()
driver.find_element(By.CSS_SELECTOR, '.display-flex button').click()
driver.find_elements(By.CSS_SELECTOR, 'form footer .display-flex button')[1].click()
additional = driver.find_element(By.NAME,
                                 "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3223387506,65549323,"
                                 "numeric)")
additional.send_keys('3')
additional.send_keys(Keys.RETURN)
time.sleep(10)
driver.quit()
