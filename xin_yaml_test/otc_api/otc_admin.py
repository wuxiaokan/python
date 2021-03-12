import sys
from otc_api import client

sys.path.append("..")
from common.read_yaml import ReadYaml

data = ReadYaml("data.yml").get_yaml_data()  # 读取数据


class OtcAdmin(client.HttpClient):
    http_map = {
        "admin_login": "dan_jiekou",  # 管理员登录
        "draw_list": "api/v1/odin/otc_ader_withdraw",  # 获取提币申请列表
        "update_draw_status": "api/v1/odin/otc_ader_withdraw/id/{}",  # 修改提币申请状态
        "get_merchant_info": "api/v1/odin/merchant",  # 获取企业平台信息
        "get_recharge_transac_list": "api/v1/odin/get_recharge_bill",  # 获取出售广告交易对账
        "get_withdraw_transac_list": "api/v1/odin/get_withdraw_bill",

        "admin_login0": "auth/api/sys/login",  # 后台登录
        "admin_duanxin_yzm": "notify/api/v1/memsms/list",  # 后台登录

    }

    def __init__(self):
        self.host = data['otc_admin_host']

    def admin_login(self, username, password, code):
        body = {
            "admin_name": username,
            "admin_passwd": password,
            "admin_captcha": code
        }
        url = self.get_full_url(self.http_map["admin_login"])
        return self.send(url, body, method="post")

    def admin_get_draw_order(self, otc_ader_id, status, session):
        etc = {
            "start": 0,
            "limit": 10,
            "otc_ader_id": otc_ader_id,
            "otc_ader_withdraw_status": status
        }
        url = self.get_full_url(self.http_map['draw_list'], etc=etc)
        return self.send(url, x_token=session)

    def admin_update_draw_status(self, id, otc_ader_id, status, session):
        body = {
            "otc_ader_withdraw_status": status,
            "otc_ader_id": otc_ader_id
        }
        url = self.get_full_url(self.http_map['update_draw_status'], replace={id})
        return self.send(url, body, method="patch", x_token=session)

    def admin_get_merchant_info(self, login_name, session):
        etc = {
            "start": 0,
            "limit": 999,
            "merchant_loginname": login_name
        }
        url = self.get_full_url(self.http_map['get_merchant_info'], etc=etc)
        return self.send(url, x_token=session)

    def admin_get_transac_list(self, session, order_number=""):
        etc = {
            "order_number": order_number
        }
        url = self.get_full_url(self.http_map['get_recharge_transac_list'], etc=etc)
        return self.send(url, x_token=session)

    def admin_get_withdraw_transac_list(self, session, order_number=""):
        etc = {
            "order_number": order_number
        }
        url = self.get_full_url(self.http_map['get_withdraw_transac_list'], etc=etc)
        return self.send(url, x_token=session)

    def admin_login0(self, username, password):
        body = {
            "username": username,
            "password": password,
            "domain": "shendu-admin-dev1.sdpjw.cn"
        }
        url = self.get_full_url(self.http_map['admin_login0'])
        return self.send(url, body, method="post")

    def admin_duanxin_yzm(self, mobile, session):
        etc = {
            "nojson": "true",
            "mobile": mobile,
            "page": 1
        }
        url = self.get_full_url(self.http_map['admin_duanxin_yzm'], etc=etc)
        return self.send(url, x_token=session)
