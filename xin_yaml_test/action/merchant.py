import allure
from otc_api import merchant
# import redis
from common.read_yaml import ReadYaml
from db.db import *
import json


class Merchant():
    def __init__(self, merchant_info):
        self.username = merchant_info['user_name']
        self.password = merchant_info['password']

        self.merchant_api_client = merchant.Merchant()
        self.session = json.dumps(self.merchant_login()['data']['token'])

    @allure.step('企业平台-登录')
    def merchant_login(self):
        return self.merchant_api_client.merchant_login(self.username, self.password)

    # 单接口登录——示例
    @allure.step('企业平台-登录')
    def merchant_login2(self, mobile, password):
        return self.merchant_api_client.merchant_login(mobile, password)

    # ------------------------------深度----------------------------------

    @allure.step("前台-获取首页")
    def get_shouye(self):
        return self.merchant_api_client.get_shouye(self.session)

    @allure.step("前台-找回密码—发送验证码")
    def zhaohui_password_fayzm(self, mobile):
        return self.merchant_api_client.zhaohui_password_fayzm(mobile)

    @allure.step("前台-找回密码")
    def zhaohui_password(self, captcha, mobile):
        return self.merchant_api_client.zhaohui_password(captcha, mobile)

    @allure.step("前台-注册")
    def zhuce(self, captcha, mobile):
        return self.merchant_api_client.zhuce(captcha, mobile)

    @allure.step("前台-找回密码—发送验证码")
    def zhuce_fayzm(self, mobile, sessionId):
        return self.merchant_api_client.zhuce_fayzm(mobile, sessionId)

    @allure.step("前台-注册—-滑动-sessionid")
    def get_zhuce_yzm__huadong_sessionID(self):
        return self.merchant_api_client.get_zhuce_yzm__huadong_sessionID()
