from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\\Development\\chromedriver.exe"
ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# CLick Sign In
sign_in = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary")
sign_in.click()

time.sleep(5)

# Enter User name and password
user_name = driver.find_element(By.ID, "username")
user_name.send_keys("*******************@*****.com")

password = driver.find_element(By.ID, "password")
password.send_keys("*****************")

# Hit Enter
password.send_keys(Keys.ENTER)

time.sleep(5)

# Open filter
open_filter = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/span/button')
open_filter.click()

time.sleep(2)

# Select last 24 hours
select_last24 = driver.find_element(By.XPATH,'//*[@id="artdeco-hoverable-artdeco-gen-42"]/div[1]/div/form/fieldset/div[1]/ul/li[4]/label/p/span[1]')
select_last24.click()

time.sleep(2)

# Hit Show Results
show_results = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span')
show_results.click()

time.sleep(2)

open_experience = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/span/button')
open_experience.click()

time.sleep(2)

experience_1 = driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-48"]/div[1]/div/form/fieldset/div[1]/ul/li[3]/label/p/span[1]')
experience_1.click()

time.sleep(1)

experience_2 = driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-48"]/div[1]/div/form/fieldset/div[1]/ul/li[4]/label/p/span[1]')
experience_2.click()

time.sleep(1)

show_results_2 = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span')
show_results_2.click()

time.sleep(2)

# Get the search results
search_results = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/header/div[1]/small').text
print(search_results)

time.sleep(2)

get_num_of_jobs = int(search_results.split(' ')[0])
num_of_pages = math.ceil(get_num_of_jobs/25)

for i in range(2, num_of_pages + 1):
    for j in range(1, 26):
       try:
           print(i)
           select_jobs = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{j}]/div/div[1]/div[1]/div[2]/div[1]/a')))
           select_jobs.click()

       except NoSuchElementException:
           pass
       else:
           time.sleep(2)
           save_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
           save_button.click()
    time.sleep(2)

    page = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[7]/ul/li[{i}]/button')
    page.click()











