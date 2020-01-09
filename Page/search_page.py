# -*- coding=utf-8 -*-
# 存储封装页面文件
import Page
from Basic.Base import Base


class Search_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)  # Base类的初始化方法

    def jump_guide(self):
        # 跳过引导页
        self.click_element(Page.guide_button)

    def input_search_text(self, text):
        """
            封装搜索按钮的输入操作
            :param text:
            :return:
        """
        # 点击首页搜索框
        self.click_element(Page.search_button)
        # 在搜索框内输入
        self.input_text(Page.search_text_box, text)
        # 点击确认按钮
        self.click_element(Page.search_confirm_button)
        # 返回到首页
        self.click_element(Page.search_text_back)
        self.click_element(Page.search_back)


