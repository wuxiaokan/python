import os
import sys

import yaml


class ReadYaml():
    def __init__(self, filename):
        self.filepath = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__)) + r"/configs/test") + "/" + filename  # 拼接定位到data文件夹
        # print("123",self.filepath)
        # D:\RJ\daima\jieKou\yaml - pytest\configs\test\data.yml
        # D:\RJ\daima\jieKou\configs / test / data.yml
        # self.filepath = os.path.join(path, 'configs/pre') + "/" + filename  # 拼接定位到data文件夹

    def get_yaml_data(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f, Loader=yaml.FullLoader)


class ReadYaml_anjiekou():
    def __init__(self, filename):
        self.filepath = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__)) + r"/data") + "/" + filename  # 拼接定位到data文件夹
        # print("123",self.filepath)
        # D:\RJ\daima\jieKou\yaml - pytest\configs\test\data.yml
        # D:\RJ\daima\jieKou\configs / test / data.yml
        # self.filepath = os.path.join(path, 'configs/pre') + "/" + filename  # 拼接定位到data文件夹

    def get_yaml_data(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    data = ReadYaml("data.yml").get_yaml_data()
    print(data)

    # D:\\RJ\\daima\\jieKou\\yaml - pytest\\testcase\\qiantai_duo_jiekou\\configs / test / data.yml
    # D:\RJ\daima\jieKou\yaml - pytest\configs\test\data.yml
