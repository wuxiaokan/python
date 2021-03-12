# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 下午 02:01
# @Author  : super man
# @FileName: run.py
# @Software: PyCharm

import pytest
import os

if __name__ == '__main__':
    # pytest.main(["-v", "-s", "../TestCase", "--html=../ui_report.html", "--self-contained-html"])  # 生成html报告
    pytest.main(["-sq", "../TestCase", "--alluredir", "../report/allure-results"])
    os.system(r"allure generate ../report/allure-results --clean -o ../report/allure-reports")  # 生成allure测试报告
