# coding=utf-8

from selenium import webdriver  # 导入selenium中的webdriver包
import time

browse = webdriver.Chrome()  # 通过webdriver调出谷歌浏览器
browse.maximize_window()  # 窗口最大化
browse.get('http://192.168.0.212/wk')


def l_submit(username, password):
    browse.find_element_by_name('name').send_keys(username)  # 输入账号
    browse.find_element_by_name('password').send_keys(password)  # 输入密码
    browse.find_element_by_name('submit').click()  # 点击登录


def l_success():
    success = browse.find_element_by_class_name('alert-success').text  # 提取文本内容
    return success


def l_success_quit():
    browse.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a/img').click()  # 点击头像
    browse.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a').click()  # 点击退出
    # time.sleep(3)
    browse.implicitly_wait(10)  # 智能等待


def l_fail():
    error = browse.find_element_by_class_name('alert-error').text  # 提取文本内容
    return error
