# coding=utf-8
from element import *


def l_success_check():
    if l_success() == u'''×\n登录成功''':
        print 'pass'
    else:
        print 'fail'


def l_fail_check():
    if l_fail() == u'''×\n用户名或密码错误！''':
        print 'pass'
    elif l_fail() == u'''×\n请正确输入用户名和密码！''':
        print 'pass'
