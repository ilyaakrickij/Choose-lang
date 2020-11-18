import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_aceert_banch(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    banch = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert True

   
