# -*- coding:utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement

from initilization.driver import Driver


class BasePage(object):

    def __init__(self):
        self.driver = Driver.driver

    def find_element(self, locate) -> WebElement:
        ele = self.driver.find_element(*locate)
        # 高亮显示
        self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,226)';", ele)
        return ele

    def find_elements(self, locate) -> WebElement:
        elements = self.driver.find_elements(*locate)
        return elements

    def switch_frame(self, frame):
        return self.driver.switch_to.frame(frame)

    def switch_window(self, window):
        self.driver.switch_to.window(window)

    def get_windows(self) -> []:
        return self.driver.window_handles

    def goto_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click_element(self, element: WebElement):
        element.click()

    def set_element_value(self, element: WebElement, key):
        element.clear()
        element.click()
        element.send_keys(key)

    def get_element_text(self, element: WebElement):
        return element.text
