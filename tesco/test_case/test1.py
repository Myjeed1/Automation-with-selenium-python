import unittest
from selenium import webdriver

from tesco.page.appl import Register


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
        self.tesco_register.ent_email("email")
        self.tesco_register.ent_password("password")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main
