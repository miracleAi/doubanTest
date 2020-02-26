# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page.basepage import BasePage


class MoviePage(BasePage):

    _movie_query = (By.ID,"inp-query")
    _movie_query_btn = (By.CLASS_NAME,"inp-btn")

    def __init__(self):
        BasePage.__init__(self)
        self.goto_movie_page()

    def goto_movie_page(self):
        pass

    def goto_main_page(self):
        pass

    def _locate_movie_query(self):
        return self.find_element(self._movie_query)

    def input_movie_query(self,name):
        self.set_element_value(self._locate_movie_query(),name)

    def _locate_movie_query_btn(self):
        return self.find_element(self._movie_query_btn)

    def click_movie_query_btn(self):
        self.click_element(self._locate_movie_query_btn())