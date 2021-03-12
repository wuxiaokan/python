# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 上午 10:38
# @Author  : super man
# @FileName: element.py
# @Software: PyCharm
from selenium import webdriver  # 导入selenium中的webdriver包

import time

browse = webdriver.Chrome()  # 通过webdriver调出谷歌浏览器
browse.maximize_window()  # 窗口最大化
browse.get('http://192.168.3.157/dongwang_admin/index.html#/dashboard')
browse.implicitly_wait(3)  # 智能等待


def l_submit(username, password):
    print(browse.title)
    browse.find_element_by_name('username').send_keys(username)  # 输入账号
    browse.find_element_by_name('password').send_keys(password)  # 输入密码
    browse.find_element_by_xpath('//*[@id="app"]/div/form/button').click()  # 点击登录
    browse.implicitly_wait(3)  # 智能等待
    successText = browse.find_element_by_class_name('sidebar-title').text  # 提取文本内容
    print(successText)
    assert (successText == '懂王app管理后台')  # 判断是否登录成功


def l_addBanner(imgUrl, title):
    browse.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div').click()
    browse.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li').click()
    browse.implicitly_wait(3)  # 智能等待
    browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/button').click()
    # 定位图片上传按钮 通过本地文件的绝对路径上传图片（r表示转移）
    browse.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/div[1]/div/input').send_keys(
        imgUrl)
    # 闪屏标题
    browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div/input').send_keys(title)

    target = browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/button')
    browse.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

    # parent = browse.find_element_by_xpath("//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div/div")
    browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div/div[1]/input').click()
    browse.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()

    # 有效时间选择
    browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div[1]/input[1]').send_keys(
        '2021-01-13 00:00:00')
    browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div/input[2]').send_keys(
        '2021-01-13 00:00:00')

    # 点击创建按钮
    browse.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/button').click()


if __name__ == '__main__':
    l_submit('wxk', '123456')
    imgUrl = 'C:/Users/Administrator.SC-201907251023/Desktop/图片魔方/banner@3x.png'
    l_addBanner(imgUrl, 'test')
