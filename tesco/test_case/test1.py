import unittest
from selenium import webdriver

from tesco.page.appl import Register
import HtmlTestRunner


class TescoRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tesco.com/")
        self.driver.maximize_window()

    def test_reg(self):
        self.tesco_register = Register(self.driver)
        self.tesco_register.cookie_tes()
        self.tesco_register.signin_tes()
        self.tesco_register.reg_acct_tes()
        self.tesco_register.ent_email("myjeed@gmail.com")
        self.tesco_register.ent_password("1234567890")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='tesco/reports'))
