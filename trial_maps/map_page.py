import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from trial_maps.map_loc import LocatorBenefit


class TestBen:
    def __init__(self, driver):
        self.driver = driver

    def test_ben2(self):
        self.driver.find_element(By.XPATH, LocatorBenefit.cookie1).click()
        # time.sleep(5)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, LocatorBenefit.benefit1).click()
        time.sleep(3)
