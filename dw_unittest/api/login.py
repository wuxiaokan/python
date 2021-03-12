# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午 04:28
# @Author  : super man
# @FileName: login.py
# @Software: PyCharm
import requests


# 登录接口
class ApiLogin(object):
    # 获取验证码
    @classmethod
    def getcode(self, url, headers, data):
        info = requests.post(url=url, headers=headers, json=data).json()
        return info

    @classmethod
    def login(self, url, headers, data):
        info = requests.post(url=url, headers=headers, json=data).json()
        return info
