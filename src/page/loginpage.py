# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from page.basepage import BasePage


class LoginPage(BasePage):
    _login_frame = (By.TAG_NAME, "iframe")
    _get_no_code = (By.CLASS_NAME, "account-form-link")
    _account_login_tab = (By.CLASS_NAME, "account-tab-account")
    _username_field = (By.CSS_SELECTOR, "#username")
    _password_field = (By.ID, "password")
    _login_btn = (By.LINK_TEXT, "登录豆瓣")
    _my_douban = (By.LINK_TEXT, "我的豆瓣")

    def __init__(self):
        BasePage.__init__(self)
        self.goto_login_page()

    def goto_login_page(self):
        self.goto_page("https://www.douban.com")

    def _locate_login_frame(self):
        return self.find_element(self._login_frame)

    def switch_to_login_frame(self):
        self.switch_frame(self._locate_login_frame())

    def _locate_no_code_link(self):
        return self.find_element(self._get_no_code)

    def _locate_account_login_tab(self):
        return self.find_element(self._account_login_tab)

    def click_account_login_tab(self):
        self.click_element(self._locate_account_login_tab())

    def _locate_username_field(self):
        return self.find_element(self._username_field)

    def input_username(self, username):
        self.set_element_value(self._locate_username_field(), username)

    def _locate_pwd_field(self):
        return self.find_element(self._password_field)

    def input_password(self, password):
        self.set_element_value(self._locate_pwd_field(), password)

    def _locate_login_btn(self):
        return self.find_element(self._login_btn)

    def click_login_btn(self):
        self.click_element(self._locate_login_btn())

    def _locate_my_douban(self):
        return self.find_element(self._my_douban)

    def get_my_douban_text(self):
        return self.get_element_text(self._locate_my_douban())

    def account_login(self, username, password):
        self.switch_to_login_frame()
        self.click_account_login_tab()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
