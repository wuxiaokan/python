# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 03:13
# @Author  : super man
# @FileName: test_login.py
# @Software: PyCharm

from PageObject.loginPage import LoginPage
from selenium import webdriver

import time


class TestLogin:
    def setup_method(self):
        # 打开浏览器,访问登录页面
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://192.168.3.157/dongwang_admin/index.html')
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        time.sleep(5)
        # 关闭浏览器
        self.driver.quit()

    # 登录成功
    def test_login_success(self):
        LoginPage(self.driver).login('wxk', '123456')
        successText = LoginPage(self.driver).get_success_info()
        self.driver.implicitly_wait(3)
        # 断言
        assert successText == '懂王app管理后台'

    # 登录失败
    def test_login_fail(self):
        LoginPage(self.driver).login('1111', '123121')
        fail_title = LoginPage(self.driver).get_title()
        self.driver.implicitly_wait(3)
        # 断言
        assert fail_title == '懂王app管理后台'
