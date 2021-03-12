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
import time
import random


@allure.feature('前台——注册')  # 测试报告显示测试功能
class Test_DengLu(base_case.BaseCase):

    @allure.title("前台——注册")
    @allure.step('注册功能')  # 测试报告显示步骤
    def test_zhuce(self, admin_action, first_ad_action):
        # 随机生成手机号
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        shoujihao = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        print(shoujihao)

        # -注册—-滑动-sessionid
        sessionId = first_ad_action.get_zhuce_yzm__huadong_sessionID()
        print(sessionId)

        # 注册 - 发送验证码
        zhuce_fayzm = first_ad_action.zhuce_fayzm(mobile=shoujihao, sessionId=sessionId)
        print(zhuce_fayzm)
        time.sleep(2)
        assert zhuce_fayzm['status_code'] == 200

        # 获取验证码
        admin_login = admin_action.admin_duanxin_yzm(mobile=shoujihao)
        yzm = admin_login['data']['page']['list'][0]['content'][23:29]
        # print(admin_login['data']['page']['list'][0])
        print(yzm)
        # 注册
        zhuce = first_ad_action.zhuce(captcha=yzm, mobile=shoujihao)
        print(zhuce)


if __name__ == "__main__":
    pytest.main(['-s', r'D:\RJ\daima\jieKou\yaml-pytest\case\qiantai_duo_jiekou\03_zhuce\test_01zhuce.py'])
