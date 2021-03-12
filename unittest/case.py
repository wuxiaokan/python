# coding=utf-8
from unittest import TestCase
from data import *
from check import *
from element import *


class Login(TestCase):
    @classmethod
    def setUpClass(self):  # TestCase类中封装的初始化方法，在每个类执行前执行一次
        self.n = 0

    @classmethod
    def setUp(self):  # TestCase类中封装的初始化方法，在每个用例执行前执行一次
        l_submit(readExcek('login', self.n, 0), readExcek('login', self.n, 1))
        self.n = self.n + 1

    def test1(self):
        l_success_check()
        l_success_quit()

    def test2(self):
        l_success_check()
        l_success_quit()

    def test3(self):
        l_fail_check()

    def test4(self):
        l_fail_check()
