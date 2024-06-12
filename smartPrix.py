from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

s = Service("C:/Users/goodb/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")

driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://www.smartprix.com/mobiles')

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
counter = 1

while True:

    driver.find_element(by=By.XPATH, value='// *[ @ id = "app"] / main / div[1] / div[2] / div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

