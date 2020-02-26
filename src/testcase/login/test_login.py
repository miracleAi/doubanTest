# -*- coding:utf-8 -*-
from page.loginpage import LoginPage
import pytest
from initilization.driver import Driver


class TestLogin(object):

    @pytest.fixture(scope="moudle", autouse=True)
    def set_up(self):
        Driver.init_driver()
        yield
        Driver.driver.quit()

    def test_login(self):
        self.login_page = LoginPage()
        print(self.login_page.get_title())
        self.login_page.account_login("13061481781", "doubanbelle1015")
        assert self.login_page.get_my_douban_text() == "我的豆瓣"
