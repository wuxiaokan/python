import sys
from otc_api import client

sys.path.append("..")
import time
import random
from util.util import Util
import uuid
import json
from common.read_yaml import ReadYaml

data = ReadYaml("data.yml").get_yaml_data()  # 读取数据


class Merchant(client.HttpClient):
    http_map = {
        "create_order": "web/api/pay",  # 创建订单
        "confirm_order": "web/view/otc_ader/id/{}/_pay",  # 订单确认打款
        "get_ad_pay_info": "web/view/otc_ader_account/id/{}",  # 通过订单信息获取广告支付信息
        "get_finance_list": "api/v1/web/merchant_finance_history",  # 获取订单历史记录
        "create_session_code": "api/v1/web/code_session",  # 生成图形验证码session
        "create_code": "api/v1/web/check_code",  # 生成验证码
        # "merchant_login":"inter-user/user/login",  # 商户登录
        "merchant_login": "auth/api/login",  # 商户登录
        "refund": "web/api/refund",  # 提现
        "add_pay_info": "api/v1/web/merchant_account",  # 添加支付方式
        "allow_order": "web/view/otc_ader/id/{}/_finish",  # 企业平台确认放币

        "get_shouye": "notify/api/v1/memmsg/getUnReadCount",  # 首页样式
        "zhaohui_password": "user/noauth/api/v1/retrPwdAndSetPwd",  # 找回密码
        "zhaohui_password_fayzm": "user/noauth/api/v1/retrPwdGetTelCaptcha",  # 找回密码_发送验证码
        "zhuce": "user/noauth/api/v1/register",  # 注册
        "zhuce_fayzm": "user/noauth/api/v1/registerGetTelCaptcha",  # 注册_发送验证码
        "get_zhuce_yzm__huadong_sessionID": "https://cf.aliyun.com/nocaptcha/analyze.jsonp",  # 注册_发送验证码

    }

    def __init__(self):
        self.host = data['merchant_host']

    # def add_pay_info(self,pay_type,account_info,status,session):
    #     merchant_account_type_name = ""
    #     if pay_type == 3:
    #         merchant_account_type_name = "Bank"
    #     body = {
    #         "merchant_account_type":pay_type,
    #         "merchant_account_type_name":merchant_account_type_name,
    #         "merchant_account_info":account_info,
    #         "merchant_account_status":status
    #     }
    #     url = self.get_full_url(self.http_map['add_pay_info'])
    #     return self.send(url,body,method="post",sessions=session)
    #
    # def allow_order(self,transac_id,order_number):
    #     etc = {
    #         "order_number":order_number
    #     }
    #     url = self.get_full_url(self.http_map['allow_order'],etc=etc,replace={transac_id})
    #     return self.send(url,method="post")
    def merchant_login(self, username, password):
        # etc = {
        #     "text": username,
        #     "password": password,
        #     "channel": 0,
        #     "gqchannel": "iosTF",
        #     "pkg": "xqty",
        #     "platform": 1,
        #     "version": "2.2.0"
        # }
        body = {
            "mobile": username,
            "password": password,
            "type": 1,
            "sig": "",
            "sessionId": "",
            "token": "",
            "scene": "",
            "directLogin": "false"
        }
        url = self.get_full_url(self.http_map['merchant_login'], h=self.host)
        print("211551551", url)
        print(body)
        return self.send(url, body, method="post")

    def get_shouye(self, session):
        url = self.get_full_url(self.http_map['get_shouye'])
        return self.send(url, x_token=session)

    # 找回密码——发送验证码
    def zhaohui_password_fayzm(self, mobile):
        body = {
            "messageType": 0,
            "mobile": mobile,
        }
        url = self.get_full_url(self.http_map['zhaohui_password_fayzm'], h=self.host)
        return self.send(url, body, method="post")

    # 注册——发送验证码
    def zhuce_fayzm(self, mobile, sessionId):
        body = {
            "messageType": 0,
            "mobile": mobile,
            "sig": " ",
            "sessionId": sessionId,
            "token": " ",
            "scene": "nc_message"
        }
        url = self.get_full_url(self.http_map['zhuce_fayzm'], h=self.host)
        print(body)
        return self.send(url, body, method="post")

    # 找回密码
    def zhaohui_password(self, captcha, mobile):
        body = {
            "captcha": captcha,
            "mobile": mobile,
            "password": 123456,
            "rePassword": 123456,
        }
        print(body)
        url = self.get_full_url(self.http_map['zhaohui_password'], h=self.host)
        return self.send(url, body, method="post")

    # 注册
    def zhuce(self, captcha, mobile):
        body = {
            "captcha": captcha,
            "mobile": mobile,
            "channel": 1,
            "inviteCode": "null",
            "name": "",
            "password": 123456,
            "rePassword": 123456,
        }
        print(body)
        url = self.get_full_url(self.http_map['zhuce'], h=self.host)
        return self.send(url, body, method="post")

    # 获取注册——发送验证码——滑动的sessionID
    def get_zhuce_yzm__huadong_sessionID(self):
        url = self.get_full_url(self.http_map['get_zhuce_yzm__huadong_sessionID'], h=self.host)
        return self.send(url, method="get")
