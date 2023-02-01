import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from trial_maps.map_page import TestBen


class TestBenefit:

    @pytest.fixture
    def setup(self):
        global driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.moneyhelper.org.uk/en")
        print(self.driver.title)
        self.driver.maximize_window()
        time.sleep(10)

        yield
        self.driver.quit()

    def test_tc1(self, setup):
        self.test_benefit = TestBen(self.driver)
        self.test_benefit.test_ben2()
