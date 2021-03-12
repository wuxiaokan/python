import sys

import allure
import pytest

sys.path.append("..")
from util.util import Util
from decimal import Decimal
from const import status_code, bs_code
from action import otc
from otc_api.otc import *


@allure.feature('首页')  # 测试报告显示测试功能
class Test():
    # OtcClient=OtcClient()

    @allure.title("交易大厅-页面正常打开")
    @allure.step('交易大厅-页面正常打开')  # 测试报告显示步骤
    def test_denglu(self, first_ad_action):
        ##首页
        shouye = first_ad_action.get_shouye()
        print("首页：", shouye)
        assert shouye['status_code'] == 200
        assert shouye['data']['msg'] == 'success'

        # # print(self.OtcClient.get_full_url(self.http_map['passwd']))
        # # code = three_ad_action.google_code(google_info['safe_secret'])
        # new_update_passwd_info = first_ad_action.update_passwd(passwd_old, passwd_new, code)
        # print(passwd_old, passwd_new, code)
        # print(new_update_passwd_info)
        # self.catch(new_update_passwd_info["status_code"] == 200, _except, status_code.OTC_UPDATA_PASSWD)


if __name__ == "__main__":
    pytest.main(['-s', r'D:\RJ\daima\xin_yaml_test\case\qiantai_duo_jiekou\01_yangshi\test_01shouye.py'])
