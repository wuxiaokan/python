# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 下午 03:58
# @Author  : super man
# @FileName: advPage.py
# @Software: PyCharm
from PageObject.basePage import Page
from PageLocators.AdvPageLoc import AdvPageLoc as loc
import allure


@allure.feature('添加闪屏模块')
class AdvPage(Page):
    # 添加闪屏
    @allure.story('添加闪屏')
    def addAdv(self, time, img_url, title, h5_url, start_time, end_time):
        with allure.step("展开app配置列表"):
            self.click(loc.app_setting_loc)
        with allure.step("点击闪屏配置"):
            self.click(loc.adv_setting_loc)
        with allure.step("点击新增闪屏"):
            self.click(loc.add_adv_loc)
        with allure.step("点击停用"):
            self.click(loc.out_enable_loc)
        with allure.step("显示双端"):
            self.click(loc.double_loc)
        with allure.step("设置闪屏时长"):
            self.input_text(loc.time_loc, time)
        with allure.step("上传图片"):
            self.input_text(loc.image_loc, img_url)
        with allure.step("闪屏标题"):
            self.input_text(loc.title_loc, title)
        with allure.step("下拉滚动条"):
            self.scroll_IntoView(loc.establish_adv_loc)
        with allure.step("选择跳转h5"):
            self.click(loc.h5_loc)
        with allure.step("输入h5链接"):
            self.input_text(loc.h5_link_loc, h5_url)
        with allure.step("输入开始时间"):
            self.input_text(loc.start_time_loc, start_time)
        with allure.step("输入结束时间"):
            self.input_text(loc.end_time_loc, end_time)
        with allure.step("点击创建闪屏"):
            self.click(loc.establish_adv_loc)

    # 获取断言
    def get_assert(self):
        return self.get_title()
