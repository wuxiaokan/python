# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 上午 11:07
# @Author  : super man
# @FileName: get_yamlData.py
# @Software: PyCharm

import yaml
import os


# 读取login.yaml文件
class GetYaml(object):
    def __init__(self, filename):
        # 获取当前路径的上级路径
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.filepath = path + '/data' + filename

    def get_yaml(self):
        with open(self.filepath, "r", encoding='utf-8') as file:
            data = yaml.full_load(file)
            return data


if __name__ == '__main__':
    GetYaml('/login.yaml').get_yaml()
