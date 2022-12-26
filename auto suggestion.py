import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def tesco_auto_sug():
    driver = webdriver.Chrome()
    url = "https://www.tesco.com/"
    driver.get(url)
    print(driver.title)
    driver.maximize_window()

    driver.implicitly_wait(10)
    search = driver.find_element(By.XPATH, "//input[@id='beans-masthead-desktop-search-input']")
    search.send_keys("Honey")
    time.sleep(10)

    h = driver.find_element(By.XPATH, '//*[@id="honey roast ham_id"]')
    h.click()
    time.sleep(3)

    try:
        search1 = driver.find_element(By.XPATH, '//*[@id="header"]/header/div/div[2]/div/div/div['
                                                '1]/div/div/div/div/div/div/div/div[2]/div[2]/button')
        search1.click()
    except NoSuchElementException:
        print("error has been handled")

    time.sleep(20)


tesco_auto_sug()
