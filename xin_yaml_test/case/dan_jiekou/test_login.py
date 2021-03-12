import allure
import requests
import pytest
from testcase.conftest import *
from common.read_yaml import *
from action.dan_merchant import Dan_Merchant
import json

testdata = ReadYaml_anjiekou('login_data.yml').get_yaml_data()  # 读取数据


@allure.feature('登录测试用例接口')  # 测试报告显示测试功能
class Test_login():
    '''测试登录接口'''

    # log = Log()
    @pytest.mark.parametrize("username,password,expect", testdata["test_login_data"],
                             ids=["正常登录"
                                  # ,
                                  #   "密码为空登录",
                                  #   "账号为空登录",
                                  #   "账号错误登录",
                                  #   "密码错误登录",
                                  #   "账号存在空格登录",
                                  #   "密码存在空格登录",
                                  #   "账号存在特殊符号登录",
                                  #   "密码存在特殊符号登录",
                                  #   "账号不完整登录",
                                  #   "密码不完整登录"
                                  ])  # 参数化测试用例
    @allure.step('账号，密码登录')  # 测试报告显示步骤
    @allure.link('http://**********:6009/api/v1/dan_jiekou', name='测试接口')  # 测试报告显示链接
    def test_login(self, username, password, expect):
        ##登录
        login = Dan_Merchant().merchant_login2(username, password)
        # print(type(login))
        print(login)
        assert str(expect['status_code']) in str(login['status_code'])  # 断言验证是否通过
        assert str(expect['msg']) in str(login['data']['msg'])  # 断言验证是否通过


if __name__ == "__main__":
    pytest.main(['-s', r'D:\RJ\daima\xin_yaml_test\case\dan_jiekou\test_login.py'])
