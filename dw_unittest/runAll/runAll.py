# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午 04:24
# @Author  : super man
# @FileName: runAll.py
# @Software: PyCharm

import pytest
import os
from dw_unittest.common.send_email import send_email

if __name__ == '__main__':
    # pytest.main(["-sq", "../testcase", "--alluredir", "../allure-results"])
    # os.system(r"allure generate ../allure-results --clean -o ../reports") # 生成allure测试报告

    pytest.main(["-sq", "../testcase", "--html", "../report.html", "--self-contained-html"])  # 生成html报告
    send_email()  # 发送测试报告邮件
