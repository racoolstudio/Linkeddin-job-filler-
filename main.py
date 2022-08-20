import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

link = 'https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3205625159&f_AL=true&geoId=104233796' \
       '&keywords=security&location=St%20John%E2%80%99s%2C%20Newfoundland%20and%20Labrador%2C%20Canada&refresh=true' \
       '&sortBy=R&start=125 '
chrome_driver_path = '/Users/racool/Desktop/chromedriver'
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
driver = webdriver.Chrome(chrome_driver_path)
driver.get(link)
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
driver.find_element(By.ID, 'username').send_keys(username)
p = driver.find_element(By.ID, 'password')
p.send_keys(password)

p.send_keys(Keys.RETURN)
time.sleep(10)
list_of_job = [job.get_attribute('href') for job in
               driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container li div div div .mr1 .disabled')]

time.sleep(2)
for i in range(len(list_of_job)):

    driver.get(list_of_job[i])
    time.sleep(3)
    try:
        driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button').click()
    except NoSuchElementException:
        print('Already Applied For')
    else:
        time.sleep(2)
        submit = driver.find_element(By.CSS_SELECTOR, '.pv4 button')

        if submit.text == 'Submit application':
            submit.click()
            print('Successfully Applied ')
        else:
            print(f'too many steps ')
            driver.get(link)

# driver.find_element(By.CLASS_NAME, 'jobs-s-apply').click()
# driver.find_element(By.CSS_SELECTOR, '.display-flex button').click()
# driver.find_elements(By.CSS_SELECTOR, 'form footer .display-flex button')[1].click()
# additional = driver.find_element(By.NAME,
#                                  "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3223387506,65549323,"
#                                  "numeric)")
# additional.send_keys('3')
# additional.send_keys(Keys.RETURN)
time.sleep(10)
