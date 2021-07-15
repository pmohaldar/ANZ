from selenium import webdriver
from base_helper import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())