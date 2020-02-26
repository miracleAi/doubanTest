# -*- coding:utf-8 -*-
import allure

from page.bookpage import BookPage
import pytest


@allure.feature("我的书籍")
class TestBooks(object):
    @allure.story("书籍查询")
    def test_query_books(self):
        book_page = BookPage()
        book_page.query_book("使用Python进行数据分析")
        with allure.step('校验结果'):
            assert "Wes McKinney" in book_page.get_auther_txt()
