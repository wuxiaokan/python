import sys
import time
import allure
import pytest

sys.path.append("..")
from util.util import Util
from decimal import Decimal
from const import status_code, bs_code

from action import otc
from otc_api.otc import *


@allure.feature('找回密码')  # 测试报告显示测试功能
class Test():
    # OtcClient=OtcClient()

    @allure.title("找回密码")
    @allure.step('找回密码')  # 测试报告显示步骤
    def test_denglu(self, first_ad_action, admin_action):
        # 找回密码 - 发送验证码
        zhaohui_password_fayzm = first_ad_action.zhaohui_password_fayzm(mobile=18821768014)
        print(zhaohui_password_fayzm)
        time.sleep(2)
        assert zhaohui_password_fayzm['status_code'] == 200

        # 获取验证码
        admin_login = admin_action.admin_duanxin_yzm(mobile=18821768014)
        yzm = admin_login['data']['page']['list'][0]['content'][23:29]
        # print(admin_login['data']['page']['list'][0])
        print(yzm)
        # 找回密码
        zhaohui_password = first_ad_action.zhaohui_password(captcha=yzm, mobile=18821768014)
        print(zhaohui_password)
        # print(admin_login)
        # print(admin_login['data']['page']['list'][0]['content'])
        # print(admin_login['data']['page']['list'][0]['content'][23:29])
        assert zhaohui_password['status_code'] == 200
        assert zhaohui_password['data']['msg'] == '验证码错误'


if __name__ == "__main__":
    pytest.main(['-s', r'D:\RJ\daima\xin_yaml_test\case\qiantai_duo_jiekou\01_yangshi\test_03zhaohuimima.py'])
