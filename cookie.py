import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def cookie_maps():
    driver = webdriver.Chrome()
    url = "https://www.moneyhelper.org.uk/en"
    driver.get(url)
    print(driver.title)
    driver.maximize_window()

    time.sleep(5)
    cookie = driver.find_element(By.XPATH, '//*[@id="ccc-notify-accept"]')
    cookie.click()

    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@title='Money troubles']").click()

    time.sleep(5)
    driver.find_element(By.XPATH, "//span[@class='cmp-header__submenu-tools-items-item-link-title'][normalize-space("
                                  ")='Debt advice locator']").click()
    time.sleep(5)

    element = driver.find_element(By.XPATH, "//a[@aria-label='Find a free debt adviser near you, online or on the "
                                            "phone']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    time.sleep(5)

    try:
        element1 = driver.find_element(By.XPATH, '//*[@id="organisation_search_query"]')
        driver.execute_script("arguments[0].scrollIntoView();", element1)
        element1.send_keys("CM2 6ND")
    except NoSuchElementException:
        print("web pass")
    time.sleep(10)


cookie_maps()
