# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 下午 02:52
# @Author  : super man
# @FileName: index.py
# @Software: PyCharm

import requests


# 首页
class ApiIndex(object):
    # 首页标签信息列表
    @classmethod
    def index_title(self, url, headers):
        info = requests.get(url=url, headers=headers).json()
        return info


if __name__ == '__main__':
    ApiIndex().index_title()
