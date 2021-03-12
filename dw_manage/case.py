# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 上午 11:05
# @Author  : super man
# @FileName: testcase.py
# @Software: PyCharm
from element import *


class Login:
    @classmethod
    def setUp(username, password):  # TestCase类中封装的初始化方法，在每个用例执行前执行一次
        l_submit(username, password)


if __name__ == 'main':
    Login.setUp('wxk', '123456')
