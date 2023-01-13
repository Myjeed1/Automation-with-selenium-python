from selenium.webdriver.common.by import By

from pytest_demo1.locator.loc import Locator


class Benefit:
    def __init__(self, driver):
        self.diver.find_element(By.XPATH, Locator.cookie1).click()

