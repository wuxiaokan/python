# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午 05:03
# @Author  : super man
# @FileName: test_login.py
# @Software: PyCharm
from api.login import ApiLogin
import pytest
import allure
from dw_unittest.common.get_yamlData import GetYaml
from common.logger import mylogger

# 获取测试用例数据
datas_dict = GetYaml('/login.yaml').get_yaml()['getCode']
common_data = GetYaml('/login.yaml').get_yaml()['common']
login_data = GetYaml('/login.yaml').get_yaml()['login']
url = common_data['url']
headers = {"Content-Type": "application/json"}
log = mylogger().loging()


@allure.feature("登录模块")
class TestLogin(object):
    @pytest.mark.parametrize("data", datas_dict)
    @allure.story("获取短信接口")
    def test_get_code(self, data, login):
        print(login)
        result = ApiLogin.getcode(url, headers, data['json'])
        print(result)
        log.info('获取短信接口日志信息: %s' % result)
        # 断言验证
        assert (result['code'] == data['expected']['status_code'])
        assert (result['message'] == data['expected']['message'])

    @allure.story("短信登录成功")
    def test_login_right(self):
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
        print(result)
        log.info('正确短信验证码验证: %s' % result)
        assert (result['code'] == 200)
        assert (result['message'] == '请求成功')

    @pytest.mark.parametrize("data", login_data)
    @allure.story("错误验证码")
    def test_login_fail(self, data, login):
        result = ApiLogin.login(data['url'], headers, data['json'])
        print(login)
        print(result)
        log.info('错误短信验证码验证: %s' % result)
        assert (result['code'] == data['expected']['status_code'])
        assert (result['message'] == data['expected']['message'])


if __name__ == "__main__":
    pytest.main(["-s", "test_login.py"])
