import time

from selenium.webdriver.common.by import By

from tesco.locator.locate import AllLocator


class Register:
    def __init__(self, driver):
        self.driver = driver

    def cookie_tes(self):
        self.driver.find_element(By.XPATH, AllLocator.cookie_tesco).click()
        time.sleep(5)

    def signin_tes(self):
        self.driver.find_element(By.XPATH, AllLocator.sign_in).click()
        time.sleep(5)

    def reg_acct_tes(self):
        self.driver.find_element(By.XPATH, AllLocator.reg_acct).click()
        time.sleep(5)

    def ent_email(self, email):
        self.driver.find_element(By.XPATH, AllLocator.enter_email).send_keys("myjeed1@gmail.com")
        time.sleep(5)

    def ent_password(self, password):
        self.driver.find_element(By.XPATH, AllLocator.enter_password).send_keys("123567890")
        time.sleep(5)

