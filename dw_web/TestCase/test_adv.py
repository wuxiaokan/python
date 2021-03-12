# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 05:02
# @Author  : super man
# @FileName: test_adv.py
# @Software: PyCharm
from PageObject.advPage import AdvPage
from PageObject.loginPage import LoginPage
from selenium import webdriver
import time

data = {
    'time': 3,
    'img_url': 'C:/Users/Administrator.SC-201907251023/Desktop/图片魔方/banner@3x.png',
    'title': 'test',
    'h5_url': 'http://www.baidu.com',
    'start_time': '2021-01-13 00:00:00',
    'end_time': '2021-01-14 00:00:00'
}


class TestAdv:
    def setup_method(self):
        # 打开浏览器,访问登录页面
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://192.168.3.157/dongwang_admin/index.html')
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        time.sleep(5)
        # 关闭浏览器
        self.driver.quit()

    def test_addAdv(self):
        LoginPage(self.driver).login('wxk', '123456')
        AdvPage(self.driver).addAdv(data['time'], data['img_url'], data['title'], data['h5_url'], data['start_time'],
                                    data['end_time'])
