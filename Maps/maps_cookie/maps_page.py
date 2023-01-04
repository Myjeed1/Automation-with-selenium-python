import time

from selenium.webdriver.common.by import By
from Maps.Maps_locators.locators import MapsLocator


class MapsTest:

    def __init__(self, driver):
        self.driver = driver
        time.sleep(5)

    def enter_cookie(self):
        self.driver.find_element(By.XPATH, MapsLocator.cookie).click()
        time.sleep(3)

    def click_benefit(self):
        self.driver.find_element(By.XPATH, MapsLocator.benefit).click()
        time.sleep(10)
