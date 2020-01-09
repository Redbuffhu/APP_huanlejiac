# -*- coding=utf-8 -*-

from Basic.Init_Driver import init_hlj_driver
from Page.search_page import Search_Page


class Test_Base(object):

    # 初始化手机驱动
    def __init__(self):
        self.driver = init_hlj_driver()

    def test_search(self, text):
        # 实例化页面封装类
        sp = Search_Page(self.driver)
        # 调用操作类
        sp.input_search_text(text)
        # 退出driver对象
        sp.driver.quit()


if __name__ == "__main__":
    Test_Base().test_search('H')

