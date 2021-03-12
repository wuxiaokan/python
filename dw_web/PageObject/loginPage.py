# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 02:50
# @Author  : super man
# @FileName: loginPage.py
# @Software: PyCharm
from PageLocators.LoginPageLoc import LoginPageLoc as loc
from PageObject.basePage import Page
import allure


@allure.feature('登录模块')
class LoginPage(Page):
    # 登录
    @allure.story('登录操作')
    def login(self, username, password):
        # 输入用户名
        with allure.step('输入用户名'):
            self.input_text(loc.user_loc, username)
        # 输入密码
        with allure.step('输入密码'):
            self.input_text(loc.password_loc, password)
        # 点击登录按钮
        with allure.step('点击登录按钮'):
            self.click(loc.login_loc)

    # 获取登录成功信息
    @allure.step('获取登录成功信息')
    def get_success_info(self):
        return self.get_text(loc.success_loc)

    # 获取登录失败信息
    @allure.step('获取登录失败信息')
    def get_fail_title(self):
        return self.get_title()
