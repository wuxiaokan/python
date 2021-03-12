import sys
from otc_api import client

sys.path.append("..")
from common.read_yaml import ReadYaml

data = ReadYaml("data.yml").get_yaml_data()  # 读取数据


class OtcClient(client.HttpClient):
    http_map = {
        "merchant_login": "api/v1/web/otc_ader/_login",  # 商户账号登录
        "get_order_list": "web/view/otc_ad/rob/adlist",  # 获取公共订单列表
        "input_google_code": "api/v1/web/otc_ader/_login/safe",  # 输入谷歌验证码
        "draw_check_phone": "api/v1/web/otc_ader/drawcheckphone",  # 划转目标账号校验
        "draw_to_phone": "api/v1/web/otc_ader/drawtophone",  # 划转到目标账号
        "get_finance": "api/v1/web/otc_ader_finance",  # 获取资产信息
        "get_finance_history_list": "api/v1/web/otc_ader_finance_history",  # 获取交易历史列表
        "get_identify_info": "api/v1/web/otc_ader/identify/phone/{}",  # 获取认证信息
        "identify": "/api/v1/web/otc_ader/level1/auth",  # 用户初级认证
        "draw_coin": "api/v1/web/otc_ader_withdraw",  # 申请体现
        "pay_list": "api/v1/web/otc_ader_account/type",  # 获取支付信息列表
        "coin_price": "api/v1/web/coin/price",  # 获取币汇率
        "create_ad": "api/v1/web/otc_ad",  # 创建广告
        "add_account_pay_info": "api/v1/web/otc_ader_account",  # 添加支付方式
        "get_pay_info_list": "api/v1/web/otc_ader_account",  # 获取支付方式列表
        "create_ader": "api/v1/web/otc_ader/register",  # 账号注册
        "get_ad_list": "api/v1/web/otc_ad",  # 获取广告列表
        "update_ad_status": "api/v1/web/otc_ad/id/{}",  # 修改广告状态
        "rob_order": "web/view/otc_ader/rob",  # 商户抢单
        "finish_order": "web/view/otc_ader/id/{}/_finish",  # 确认放币
        "get_transac_list": "api/v1/web/otc_transac",  # 获取交易订单列表
        "confirm_pay": "web/view/otc_ader/id/{}/_pay",  # 确认付款
        "passwd": "api/v1/web/otc_ader/update_passwd",  # 修改APP密码
        "get_transac_list11111": "/shcpe-cos/bill/status?yikikata=74d38ac5-205218fd91625e31e1ec0ab84dab7551"
        # 修改APP密码11

    }

    def __init__(self):
        self.host = data['otc_app_host']

    # def ping(self):
    #     fullUrl =self.get_full_url(self.http_map["ping"])
    #     return self.send(fullUrl)
    # def post_test(self,body):
    #     fullUrl = self.get_full_url(self.http_map["intSet"])
    #     return self.send(fullUrl,body,"post")

    def merchant_login(self, user_name, password):
        body = {
            "mobile": user_name,
            "password": password,
            "type": 1,
            "sig": "",
            "sessionId": "",
            "token": "",
            "scene": "",
            "directLogin": "false"
        }
        url = self.get_full_url(self.http_map['merchant_login'])
        print(body)
        print(url)
        return self.send(url, body, 'post')

    def get_order_list(self, session):
        url = self.get_full_url(self.http_map['get_order_list'])
        return self.send(url, sessions=session)

    def input_google_code(self, code, session):
        url = self.get_full_url(self.http_map['input_google_code'])
        body = {
            "google_authenticator": str(code)
        }
        return self.send(url, body, sessions=session, method="post")

    def transfer(self, session, num, target, code, coin_name):
        body = {
            "coin_name": coin_name,
            "amount": str(num),
            "recipient_phone": target,
            "google_authenticator": code
        }
        url = self.get_full_url(self.http_map['draw_to_phone'])
        return self.send(url, body, sessions=session, method="post")

    def draw_phone_check(self, session, phone):
        body = {
            "recipient_phone": phone
        }
        url = self.get_full_url(self.http_map['draw_check_phone'])
        return self.send(url, body, sessions=session, method="post")

    def get_finance(self, session):
        url = self.get_full_url(self.http_map['get_finance'])
        return self.send(url, sessions=session)

    def get_finance_history_list(self, session, coin_id):
        etc = {
            "coin_id": coin_id,
            "start": 1,
            "limit": 10
        }
        url = self.get_full_url(self.http_map['get_finance_history_list'], etc)
        return self.send(url, sessions=session)

    def get_identify_info(self, session, phone):
        url = self.get_full_url(self.http_map['get_identify_info'], replace={phone})
        return self.send(url, sessions=session)

    def identify(self, kyc_id, kyc_name, area, phone, session):
        body = {
            "country": area,
            "phone": phone,
            "identity_card": kyc_id,
            "name": kyc_name
        }
        url = self.get_full_url(self.http_map['identify'])
        return self.send(url, body, sessions=session, method="post")

    def draw_coin(self, addr, num, coin_name, code, session):
        body = {
            "coin_name": coin_name,
            'amount': str(num),
            "otc_ader_withdraw_addr": addr,
            "check_token": code
        }
        url = self.get_full_url(self.http_map['draw_coin'])
        return self.send(url, body, sessions=session, method="post")

    def get_account_type(self, session):
        url = self.get_full_url(self.http_map['pay_list'])
        return self.send(url, sessions=session)

    def get_coin_price(self, session, price_type):
        etc = {
            "price_type": price_type
        }
        url = self.get_full_url(self.http_map['coin_price'], etc=etc)
        return self.send(url, sessions=session)

    def create_ad(self, coin_name, ad_type, is_bank, is_alipay, is_wechatpay, amount, min_limit, max_limit, session):
        body = {
            "coin_name": coin_name,
            "otc_ad_type": ad_type,
            "is_bank": is_bank,
            "amount": amount,
            "min_limit": min_limit,
            "max_limit": max_limit,
            "is_alipay": is_alipay,
            "is_wechatpay": is_wechatpay
        }
        url = self.get_full_url(self.http_map['create_ad'])
        return self.send(url, body, method="post", sessions=session)

    def add_pay_type(self, type, account_info, status, session):
        otc_ad_account_type_name = ""
        if type == 3:
            otc_ad_account_type_name = "Bank"
        body = {
            "otc_ad_account_type": type,
            "otc_ad_account_type_name": otc_ad_account_type_name,
            "otc_account_info": account_info,
            "otc_account_status": status
        }
        url = self.get_full_url(self.http_map['add_account_pay_info'])
        return self.send(url, body, sessions=session, method="post")

    def get_pay_info_list(self, session):
        url = self.get_full_url(self.http_map['get_pay_info_list'])
        return self.send(url, sessions=session)

    def update_passwd(self, session, passwd_old, passwd_new, code):
        url = self.get_full_url(self.http_map['passwd'])

        body = {
            "passwd": passwd_old,
            "passwd_new": passwd_new,
            "check_token": code
        }
        print(url)
        print(body)
        return self.send(url, body, sessions=session, method="post")

    def create_ader(self, user_name, password, ader_name, invite_code):
        url = self.get_full_url(self.http_map['create_ader'])
        body = {
            "otc_ader_name": ader_name,
            "otc_ader_loginname": user_name,
            "passwd": password,
            "referral_code": invite_code
        }
        return self.send(url, body, method="post")

    def get_ad_list(self, session):
        etc = {
            "start": 1,
            "limit": 999,
        }
        url = self.get_full_url(self.http_map['get_ad_list'], etc=etc)
        return self.send(url, sessions=session)

    def update_ad_status(self, otc_ad_id, otc_ader_id, status, session):
        body = {
            "otc_ader_id": otc_ader_id,
            "otc_ad_id": otc_ad_id,
            "otc_ad_status": status,
            "min_limit": "10"  # daicaozuo
        }
        replace = {
            otc_ad_id
        }
        etc = {
            "cols": "1"
        }
        url = self.get_full_url(self.http_map['update_ad_status'], replace=replace, etc=etc)
        return self.send(url, body, method="post", sessions=session)

    def ader_rob_order(self, order_number, session):
        body = {
            "order_number": order_number
        }
        url = self.get_full_url(self.http_map['rob_order'])
        return self.send(url, body, method="post", sessions=session)

    def allow_order(self, transac_id, session):
        body = {}
        url = self.get_full_url(self.http_map['finish_order'], replace={transac_id})
        return self.send(url, body, method='post', sessions=session)

    def get_transac_list(self, session):
        etc = {
            "start": 1,
            "limit": 9999
        }
        url = self.get_full_url(self.http_map['get_transac_list'], etc=etc)
        return self.send(url, sessions=session)

    def confirm_pay(self, transac_id, session):
        url = self.get_full_url(self.http_map['confirm_pay'], replace={transac_id})
        return self.send(url, method='post', sessions=session)

    def get_transac_list111111111111(self):
        etc = {
            "acptBNKCode": "301161000061",
            "cdAmt": "159857",
            "cdNo": "230116100006120201026753056996",
            "cdTP": "AC02",
            "issDate": "2020-10-26",
            "requestNo": 1605680965499,
            "requestSystem": "shcpe-cos",
            "requestTime": "2020-11-18"
        }
        url = self.get_full_url(self.http_map['get_transac_list11111'], etc=etc)
        print(url)
        return self.send(url)
