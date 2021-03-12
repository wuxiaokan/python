import allure
from otc_api import merchant
# import redis
from common.read_yaml import ReadYaml
from db.db import *
import json


class Dan_Merchant:
    merchant_api_client = merchant.Merchant()

    # 单接口——示例
    @allure.step('企业平台-登录')
    def merchant_login2(self, username, password):
        return self.merchant_api_client.merchant_login(username, password)
