# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 下午 03:24
# @Author  : super man
# @FileName: conftest.py
# @Software: PyCharm

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    # 打开浏览器,访问登录页面
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
