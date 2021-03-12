# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 02:32
# @Author  : super man
# @FileName: basePage.py
# @Software: PyCharm
from dw_web.common.logger import mylogger

my_log = mylogger().loging()


class Page(object):
    """
        Page基类，所有page都继承此类

    """

    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def find_element(self, *loc):
        my_log.info('定位到元素{}'.format(loc))
        self.driver.implicitly_wait(3)
        return self.driver.find_element(*loc)

    # 输入框
    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)
        my_log.info('输入内容---{}'.format(text))
        self.driver.implicitly_wait(3)

    # 点击
    def click(self, loc):
        self.find_element(*loc).click()
        my_log.info('点击按钮{}'.format(loc))
        self.driver.implicitly_wait(3)

    # 文本
    def get_text(self, loc):
        my_log.info('获取文本信息---{}'.format(self.find_element(*loc).text))
        self.driver.implicitly_wait(3)
        return self.find_element(*loc).text

    # 浏览器title
    def get_title(self):
        my_log.info('获取当前页面的title----{}'.format(self.driver.title))
        self.driver.implicitly_wait(3)
        return self.driver.title

    # 滚动条拖动到可见元素
    def scroll_IntoView(self, loc):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*loc))

