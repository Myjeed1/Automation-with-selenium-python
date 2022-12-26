import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def dropdown_tesco():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://www.tesco.com/"
    driver.get(url)
    driver.implicitly_wait(20)
    print(driver.title)

    dropdown1 = driver.find_element(By.XPATH, "//a[normalize-space()='Register']")
    dropdown1.click()
    time.sleep(20)
    #driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    driver.find_element(By.CSS_SELECTOR, "#pages\.landing\.clubcard\.radio-labels\.already-have").click

    time.sleep(5)
    drop = driver.find_element(By.XPATH, "//select[@id='title']")
    tittle = Select(drop)

    tittle.select_by_value('Mrs')

    time.sleep(3)
    phone = driver.find_element(By.XPATH, "//span[contains(text(),'Create account')]")
    ActionChains(driver).scroll_to_element(phone).perform()
    time.sleep(30)


dropdown_tesco()

