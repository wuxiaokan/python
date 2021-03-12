# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 02:45
# @Author  : super man
# @FileName: LoginPageLoc.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 用户名输入框
    user_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div[1]/input')
    # 密码输入框
    password_loc = (By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input')
    # 登录按钮
    login_loc = (By.XPATH, '//*[@id="app"]/div/form/button')
    # 登录成功信息
    success_loc = (By.CLASS_NAME, 'sidebar-title')
