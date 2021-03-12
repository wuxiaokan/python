# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 下午 04:58
# @Author  : super man
# @FileName: test_elementui.py
# @Software: PyCharm
import pytest
import allure
import time


@allure.feature("后台添加闪屏")
class Testadv():
    @allure.story("后台管理登录")
    def test_login_element(self, browse):
        browse.find_element_by_name('username').send_keys('wxk')  # 输入账号
        browse.find_element_by_name('password').send_keys('123456')  # 输入密码
        browse.find_element_by_xpath('//*[@id="app"]/div/form/button').click()  # 点击登录
        browse.implicitly_wait(3)  # 智能等待
        successText = browse.find_element_by_class_name('sidebar-title').text  # 提取文本内容
        print(successText)
        assert (successText == '懂王app管理后台')  # 判断是否登录成功

    @allure.story("添加闪屏")
    def test_add_adv(self, browse):
        browse.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div').click()
        browse.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li').click()
        browse.implicitly_wait(3)  # 智能等待
        browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/button').click()
        time.sleep(1)
        text = browse.find_element_by_xpath('//*[@id="breadcrumb-container"]/span/span[3]/span[1]/span').text
        print(text)
        assert text =='新增闪屏' # 判断是否进入添加页面
        browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div/label[2]/span[2]').click()
        # 定位图片上传按钮 通过本地文件的绝对路径上传图片（r表示转移）
        browse.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/div[1]/div/input').send_keys(
            'C:/Users/Administrator.SC-201907251023/Desktop/图片魔方/banner@3x.png')
        # 闪屏标题
        browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div/input').send_keys('test')

        target = browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/button')
        browse.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

        # parent = browse.find_element_by_xpath("//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div/div")
        browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div/div[1]/input').click()
        browse.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()

        # 有效时间选择
        browse.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div[1]/input[1]').send_keys(
            '2021-01-13 00:00:00')
        browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div/input[2]').send_keys(
            '2021-01-13 00:00:00')

        # 点击创建按钮
        browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/button').click()
        time.sleep(2)
        text1 = browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/span/span/button/span').text
        assert text1 == '批量删除闪屏'

