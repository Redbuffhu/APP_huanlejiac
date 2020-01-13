# -*- coding: utf-8 -*-

import time, allure
from selenium.webdriver.support.wait import WebDriverWait
from Basic.utils import log


class ElementActions(object):
    def __init__(self, driver):
        self.driver = driver

    def get_img(self, name='App截图'):
        png_data = self.driver.get_screenshot_as_png()
        # current_time = time.strftime("_%H:%m:%s_", time.localtime(time.time()))  # linux下时间格式
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        current_name = name + current_time + ".png"
        print(current_name)

        allure.attach(png_data, name=current_name, attachment_type=allure.attachment_type.PNG)

    def sleep(self, s, islog=True):
        if islog == True:
            message = "sleep等待｛｝s".format(str(s))
            log.info(message)
        time.sleep(s)
        return self

    def find_element(self, loc, timeout=10):
        """
            二次封装find_element 方法。增加了显示等待和简化参数传递
            :param loc: 传入(By.**,'value')解包后为单独的两个值，需要传递两个值
            :param timeout: 搜寻等待时间
            :return: 返回定位到的元素对象
        """
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        """
            封装点击操作
        """
        self.find_element(loc).click()

    def input_text(self, loc, text):
        """
            封装输入文本操作
            :param text: 文本内容
        """
        self.fm = self.find_element(loc)
        self.fm.clear()
        self.fm.send_keys(text)
