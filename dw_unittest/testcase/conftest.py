# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 上午 10:05
# @Author  : super man
# @FileName: conftest.py
# @Software: PyCharm

# coding:utf-8
from selenium import webdriver  # 导入selenium中的webdriver包
import pytest
from common.get_yamlData import GetYaml
from api.login import ApiLogin

datas_dict = GetYaml('/login.yaml').get_yaml()['getCode_login']
common_data = GetYaml('/login.yaml').get_yaml()['common']
login_data = GetYaml('/login.yaml').get_yaml()['login']
headers = {"Content-Type": "application/json"}
url = common_data['url']


@pytest.fixture(scope="session")
def login():
    # 短信验证码
    sms_code = ApiLogin.getcode(url, headers, datas_dict[0]['json'])['data']['smsCode']
    phone = datas_dict[0]['json']['phone']
    right_data = {
        "type": 1,
        "flashToken": "",
        "deviceId": 1,
        "device": "1",
        "smsCode": sms_code,
        "phone": phone
    }
    result = ApiLogin.login(login_data[0]['url'], headers, right_data)
    head = {
        "Content-Type": "application/json",
        "token": result['data']['token']
    }
    return head


@pytest.fixture(scope="session")
def browse():
    browse = webdriver.Chrome()  # 通过webdriver调出谷歌浏览器
    browse.maximize_window()  # 窗口最大化
    browse.get('http://192.168.3.157/dongwang_admin/index.html#/dashboard')
    browse.implicitly_wait(3)  # 智能等待
    return browse
