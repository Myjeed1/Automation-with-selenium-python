import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.moneyhelper.org.uk/en')
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="ccc-notify-accept"]').click()
time.sleep(20)

