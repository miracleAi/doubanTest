# -*- coding:utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from page.basepage import BasePage


class BookPage(BasePage):
    _book_tab = (By.LINK_TEXT, "读书")
    _book_query = (By.ID, "inp-query")
    _book_query_btn = (By.CLASS_NAME, "inp-btn")
    # _auther_text = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[1]/div[1]/div/div/div[3]")
    _auther_text = (By.CSS_SELECTOR, ".abstract")

    def __init__(self):
        BasePage.__init__(self)
        self.goto_book_page()
        with allure.step("切换到我的书籍窗口"):
            self.switch_book_window()

    def goto_book_page(self):
        self.click_book_tab()

    def switch_book_window(self):
        windows = self.get_windows()
        self.switch_window(windows[-1])

    def goto_main_page(self):
        self.goto_page("https://www.douban.com")

    def _locate_book_tab(self):
        return self.find_element(self._book_tab)

    def click_book_tab(self):
        self.click_element(self._locate_book_tab())

    def _locate_book_query(self):
        return self.find_element(self._book_query)

    def input_book_query(self, book_name):
        self.set_element_value(self._locate_book_query(), book_name)

    def _locate_book_query_btn(self):
        return self.find_element(self._book_query_btn)

    def click_book_query_btn(self):
        self.click_element(self._locate_book_query_btn())

    def _locate_auther_text_eles(self) -> []:
        return self.find_elements(self._auther_text)

    def get_auther_txt(self):
        elementss = self._locate_auther_text_eles()

        if len(elementss) > 0:
            return self.get_element_text(elementss[0])

    def query_book(self, book_name):
        with allure.step('查询书籍'):
            self.input_book_query(book_name)
        with allure.step('点击查询'):
            self.click_book_query_btn()
