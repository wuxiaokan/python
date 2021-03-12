import allure

import sys

sys.path.append("..")
from otc_api import otc
import time
from db.db import *

from common.read_yaml import ReadYaml

data = ReadYaml("data.yml").get_yaml_data()  # 读取数据


class Otc():
    user_is_valid = True

    def __init__(self, user_info, invite_code=False, ader_name=""):
        self.username = user_info['user_name']
        self.password = user_info['password']
        self.otc_api_client = otc.OtcClient()

        if invite_code:
            rsp = self.create_user(self.username, self.password, ader_name, invite_code)
            if rsp['status_code'] != 200:
                self.user_is_valid = False
                return
        result = self.user_login()
        print(result)
        if result['status_code'] != 200:
            self.user_is_valid = False
            return
        self.otc_ader_id = result['data']['otc_ader_id']
        self.otc_ader_name = result['data']['otc_ader_name']
        self.session = result['data']['session']
        # login_status == 2 需要验证谷歌验证码
        if result['data']['login_status'] == 2:
            self.google_auth()

    def is_valid(self):
        return self.user_is_valid

    @allure.step('开始用户登录')
    def user_login(self):
        return self.otc_api_client.merchant_login(self.username, self.password)

    @allure.step("创建用户")
    def create_user(self, user_name, password, ad_name, invite_code):
        return self.otc_api_client.create_ader(user_name, password, ad_name, invite_code)

    @allure.step("创建用户验证")
    def check_create_user(self):
        pass

    @allure.step('获取订单列表')
    def get_order_list(self):
        time.sleep(1.2)  # 轮询接口 1秒延时 设置1.2秒防止限制
        return self.otc_api_client.get_order_list(self.session)

    @allure.step("广告下单")
    def create_order(self):
        pass

    @allure.step("获取谷歌验证码")
    def get_google_info(self):
        # row = self.db_conn.query("select * from t_otc_ader_safe where otc_ader_id = {}",self.otc_ader_id)
        row = sql(sql=("select * from t_otc_ader_safe where otc_ader_id = {}", self.otc_ader_id))
        return row[0]

    @allure.step('谷歌验证')
    def google_auth(self):
        code = self.get_google_code()
        return self.input_google_auth(code)

    @allure.step("获取当前谷歌验证码")
    def get_google_code(self):
        secret = self.get_google_info()['safe_secret']
        return self.google_code(secret)

    @allure.step('输入谷歌验证码')
    def input_google_auth(self, code):
        return self.otc_api_client.input_google_code(code, self.session)

    @allure.step('修改密码')
    def update_passwd(self, passwd_old, passwd_new, code):
        return self.otc_api_client.update_passwd(self.session, passwd_old, passwd_new, code)

    @allure.step("执行划转")
    def transfer(self, num, target, code, coin_name):
        return self.otc_api_client.transfer(self.session, num, target, code, coin_name)

    @allure.step("划转目标账号校验")
    def draw_phone_check(self, phone):
        return self.otc_api_client.draw_phone_check(self.session, phone)

    @allure.step("获取目标账号资产")
    def get_finance(self):
        return self.otc_api_client.get_finance(self.session)

    @allure.step("获取资产交易记录列表")
    def get_finance_history_list(self, coin_id):
        return self.otc_api_client.get_finance_history_list(self.session, coin_id)

    @allure.step('获取认证信息')
    def get_identify_info(self):
        return self.otc_api_client.get_identify_info(self.session, self.username)

    @allure.step('开始初级认证')
    def identify(self, kyc_id, kyc_name, area):
        return self.otc_api_client.identify(kyc_id, kyc_name, area, self.username, self.session)

    @allure.step("发起提币申请")
    def draw_coin(self, addr, num, coin_name, code):
        return self.otc_api_client.draw_coin(addr, num, coin_name, code, self.session)

    @allure.step("获取提币手续费信息")
    def get_draw_fee_info(self):
        return 1

    @allure.step('获取银行消息')
    def get_account_type(self):
        return self.otc_api_client.get_account_type(self.session)

    @allure.step("添加支付方式")
    def add_pay_type(self, type, account_info, status):
        return self.otc_api_client.add_pay_type(type, account_info, status, self.session)

    @allure.step("获取支付方式列表")
    def get_pay_info_list(self):
        return self.otc_api_client.get_pay_info_list(self.session)

    @allure.step('获取币信息')
    def get_coin_price(self, price_type):
        return self.otc_api_client.get_coin_price(self.session, price_type)

    @allure.step("发布广告")
    def create_ad(self, coin_name, ad_type, amount, min_limit, max_limit, is_bank=0, is_alipay=0, is_wechatpay=0):
        return self.otc_api_client.create_ad(coin_name, ad_type, is_bank, is_alipay, is_wechatpay, amount, min_limit,
                                             max_limit, self.session)

    @allure.step("获取广告列表")
    def get_ad_list(self):
        return self.otc_api_client.get_ad_list(self.session)

    @allure.step('修改广告状态')
    def update_ad_status(self, otc_ad_id, status):
        return self.otc_api_client.update_ad_status(otc_ad_id, self.otc_ader_id, status, self.session)

    @allure.step('商户抢单')
    def ader_rob_order(self, order_number):
        return self.otc_api_client.ader_rob_order(order_number, self.session)

    @allure.step('商户放币')
    def allow_order(self, transac_id):
        return self.otc_api_client.allow_order(transac_id, self.session)

    @allure.step('获取交易订单信息')
    def get_transac_list(self):
        return self.otc_api_client.get_transac_list(self.session)

    @allure.step('确认付款')
    def confirm_pay(self, transac_id):
        return self.otc_api_client.confirm_pay(transac_id, self.session)

    @allure.step('确认付款1111111111111')
    def get_transac_list111111111111(self):
        return self.otc_api_client.get_transac_list111111111111()
