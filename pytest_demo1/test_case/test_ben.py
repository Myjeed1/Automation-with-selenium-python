import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pytest_demo1.locator.loc import LocatorBenefit


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.moneyhelper.org.uk/en")
    driver.maximize_window()
    time.sleep(4)

    yield
    driver.quit()


def test_ben2(setup):
    driver.find_element(By.XPATH, LocatorBenefit.cookie1).click()
    driver.find_element(By.XPATH, LocatorBenefit.benefit1).click()
    time.sleep(3)
"""l

def test_uni(setup):
    driver.find_element(By.XPATH, LocatorBenefit.uni_credit).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_ben_child(setup):
    driver.find_element(By.XPATH, LocatorBenefit.ben_children).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_ben(setup):
    driver.find_element(By.XPATH, LocatorBenefit.ben_sick).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_later_life(setup):
    driver.find_element(By.XPATH, LocatorBenefit.ben_later_life).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_ben_work1(setup):
    driver.find_element(By.XPATH, LocatorBenefit.ben_work).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_ben_house(setup):
    driver.find_element(By.XPATH, LocatorBenefit.ben_house).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_prob_ben(setup):
    driver.find_element(By.XPATH, LocatorBenefit.prob_ben).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.back()


def test_ben_ben(setup):
    driver.find_element(By.XPATH, LocatorBenefit.benefit_ben).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    driver.back()"""
