import time

from selenium import webdriver

import unittest

from Maps.maps_cookie.maps_page import MapsTest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class CookieTest(unittest.TestCase):

    def setUp(self):
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.get('https://www.moneyhelper.org.uk/en')
        self.driver.maximize_window()

    def test_cookie(self):
        self.click_cookie = MapsTest(self.driver)
        self.click_cookie.enter_cookie()
        time.sleep(3)
        self.click_cookie.click_benefit()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
