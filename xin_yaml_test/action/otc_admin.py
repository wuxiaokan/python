import allure
import sys
import pytest

sys.path.append("..")

from otc_api import otc_admin
from common.read_yaml import ReadYaml

from db.db import *


class OtcAdmin():
    def __init__(self, admin_info):
        self.username = admin_info['user_name']
        self.password = admin_info['password']
        self.otc_admin_api_client = otc_admin.OtcAdmin()
        result = self.admin_login()
        print("result:", result)
        assert result['status_code'] == 200, "总后台管理员登录失败"
        self.session = result['data']['token']

    @allure.step("总后台账号登录")
    def admin_login(self):
        m = otc_admin.OtcAdmin()
        return m.admin_login0(self.username, self.password)

    @allure.step("总后台获取指定账号的申请订单")
    def admin_get_draw_order(self, otc_ader_id, status):
        return self.otc_admin_api_client.admin_get_draw_order(otc_ader_id, status, self.session)

    @allure.step("修改提币申请状态")
    def admin_update_draw_status(self, otc_ader_id, order_id, status):
        return self.otc_admin_api_client.admin_update_draw_status(order_id, otc_ader_id, status, self.session)

    @allure.step("获取商户手续费信息")
    def admin_get_merchant_info(self, login_name):
        return self.otc_admin_api_client.admin_get_merchant_info(login_name, self.session)

    @allure.step("获取出售广告-交易对账")
    def admin_get_transac_list(self, order_number=""):
        return self.otc_admin_api_client.admin_get_transac_list(self.session, order_number)

    @allure.step("获取购买广告-交易对账")
    def admin_get_withdraw_transac_list(self, order_number=""):
        return self.otc_admin_api_client.admin_get_withdraw_transac_list(self.session, order_number)

    @allure.step("获取短信验证码")
    def admin_duanxin_yzm(self, mobile):
        return self.otc_admin_api_client.admin_duanxin_yzm(mobile, self.session)
