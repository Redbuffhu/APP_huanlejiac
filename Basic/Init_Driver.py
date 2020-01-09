# -*- coding=utf-8 -*-
# 手机驱动对象初始化
from appium import webdriver


def init_hlj_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6'
    # 设备号
    desired_caps['deviceName'] = '192.168.99.103:5555'
    # app包名
    desired_caps['appPackage'] = 'com.xlylf.huanlejiac'
    # 启动名
    desired_caps['appActivity'] = '.ui.login.GuideActivity'
    # 允许输入中文
    desired_caps['unicodekeyboard'] = True
    desired_caps['resetkeyboard'] = True
    # 创建手机对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver


def init_set_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # 设备号
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 包名
    desired_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desired_caps['appActivity'] = '.Settings'
    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

