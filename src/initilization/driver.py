# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:

    driver = ''  # type: WebDriver

    @staticmethod
    def init_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-infobars')
        Driver.driver = webdriver.Chrome(options=chrome_options)
        Driver.driver.implicitly_wait(10)
