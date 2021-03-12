# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 下午 03:04
# @Author  : super man
# @FileName: test_index.py
# @Software: PyCharm

import pytest
import allure
from api.index import ApiIndex
from common.get_yamlData import GetYaml
from common.con_sql import *
from common.logger import mylogger

log = mylogger().loging()

# 获取测试数据
common_data = GetYaml('/index.yaml').get_yaml()['common']
url_getIndexTitle = common_data['url']


@allure.feature("首页模块")
class TestIndex(object):
    @allure.story("首页标签信息列表")
    def test_get_index_title(self, login):
        result = ApiIndex.index_title(url_getIndexTitle, login)
        # 获取数据库title列表
        sql_data = select('select tag_name from sys_tag where del=0 and home_show=0')
        sql_arr = []
        for (row,) in sql_data:
            sql_arr.append(row)
        # 接口返回值数组
        arr = []
        for i in result['data']:
            arr.append(i['tagName'])
        print(result['data'])
        log.info('首页标签信息列表:%s' % arr)
        # 断言 判断数据库数据与接口数据是否一致
        assert sql_arr == arr
