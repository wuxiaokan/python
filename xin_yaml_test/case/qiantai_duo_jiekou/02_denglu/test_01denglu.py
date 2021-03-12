import sys

import allure
import pytest

sys.path.append("..")
from util.util import Util
from decimal import Decimal
from const import status_code, bs_code
from base_class import base_case
from action import otc
from otc_api.otc import *


@allure.feature('前台——登录')  # 测试报告显示测试功能
class Test_DengLu(base_case.BaseCase):

    @allure.title("前台——登录")
    @allure.step('账号，密码正常登录')  # 测试报告显示步骤
    def test_denglu(self, first_ad_action):
        ##登录
        login = first_ad_action.merchant_login()
        print(login)
        assert login['status_code'] == 200
        assert login['data']['corpName'] == '费县永泽商贸有限公司1'


if __name__ == "__main__":
    pytest.main(['-s', r'D:\RJ\daima\jieKou\yaml-pytest\case\qiantai_duo_jiekou\02_denglu\test_01denglu.py'])
