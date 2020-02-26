# -*- coding:utf-8 -*-
import allure
import pytest
from initilization.driver import Driver
from page.loginpage import LoginPage
from configparser import ConfigParser


@pytest.fixture(scope="session", autouse=True)
def login_and_out():
    Driver.init_driver()
    login_page = LoginPage()
    cf = ConfigParser()
    cf.read("../cfg/auto.cfg")
    username = cf.get("account", "username")
    password = cf.get("account", "password")
    login_page.account_login(username, password)
    yield
    Driver.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if (rep.when == "call" or rep.when == "setup") and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""

            f.write(rep.nodeid + extra + "\n")

        pic_info = Driver.driver.get_screenshot_as_png()
        with allure.step('添加失败截图'):
            allure.attach('失败截图', pic_info, allure.attach_type.PNG)
