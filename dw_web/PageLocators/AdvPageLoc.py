# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 03:31
# @Author  : super man
# @FileName: AdvPageLoc.py
# @Software: PyCharm

from selenium.webdriver.common.by import By


class AdvPageLoc:
    # app配置展开
    app_setting_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div')
    # 闪屏配置
    adv_setting_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li')
    # 新增按钮
    add_adv_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/button')
    # 状态启用
    enable_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div/label[1]/span[2]')
    # 状态停用
    out_enable_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div/label[2]/span[2]')
    # 显示终端 -- 安卓
    android_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/label[2]/span[2]')
    # 显示终端 -- 苹果
    ios_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/label[3]/span[2]')
    # 显示终端 -- 双端
    double_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/label[1]/span[2]')
    # 闪屏时长输入框
    time_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[3]/div/div/div/input')
    # 图片上传
    image_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/div[1]/div/input')
    # 闪屏标题输入框
    title_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div[1]/input')
    # 是否跳转 -- 是
    jump_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[7]/div/div/label[1]/span[2]')
    # 是否跳转 --否
    out_jump_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[7]/div/div/label[2]/span[2]')
    # h5跳转
    h5_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[8]/div/div/label[1]/span[2]')
    # h5链接输入框
    h5_link_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/block/div/input')
    # 开始时间
    start_time_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div[1]/input[1]')
    # 结束时间
    end_time_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div[1]/input[2]')
    # 创建闪屏按钮
    establish_adv_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/form/div[11]/div/button')



