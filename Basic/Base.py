# 方法的二次封装
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):

    def __init__(self, driver):
        self.driver = driver

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

