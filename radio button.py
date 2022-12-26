import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def tesco_auto_sug():
    driver = webdriver.Chrome()
    url = 'https://www.tesco.com/groceries/en-GB/search?query=honey&icid=tescohp_sws-1_m-sug_in-honey_ab-226-b_out' \
          '-honey'
    driver.get(url)
    print(driver.title)
    driver.maximize_window()

    driver.find_element(By.XPATH, "//label[@title='Special Offers']//span[@class='checkbox-square "
                                  "checkbox-square-linked']").click()

    time.sleep(10)


tesco_auto_sug()
