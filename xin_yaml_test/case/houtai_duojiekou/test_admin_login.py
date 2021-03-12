import sys

import allure
import pytest

sys.path.append("..")
from util.util import Util
from decimal import Decimal
from const import status_code, bs_code

from action import otc
from otc_api.otc import *


@allure.feature('后台——登录')  # 测试报告显示测试功能
class Test_DengLu():

    @allure.title("后台——登录")
    @allure.step('账号，密码正常登录')  # 测试报告显示步骤
    def test_admin_login(self, admin_action):
        ##修改密码
        admin_login = admin_action.admin_login()
        print(admin_login)
        assert admin_login['status_code'] == 200
        assert admin_login['data']['msg'] == 'success'


if __name__ == "__main__":
    pytest.main(['-s', r'D:\RJ\daima\xin_yaml_test\case\houtai_duojiekou\test_admin_login.py'])
