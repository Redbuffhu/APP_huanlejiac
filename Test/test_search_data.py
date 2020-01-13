# -*- coding=utf-8 -*-

import os, sys
sys.path.append(os.getcwd())  # 告诉pytest运行前先检索当前路径
from Basic.Init_Driver import init_hlj_driver
from Basic.read_data import Read_Data
from Page.search_page import Search_Page
import pytest
import allure


"""
allure generate report/ -o report/html
"""


def package_param_data():
    # 储存参数值列表 ，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
    list_data = []
    # 返回yaml文件数据
    yaml_data = Read_Data("Search_page.yaml").return_data()
    # print(type(yaml_data))
    # print(yaml_data)
    for i in yaml_data.keys():
        # print(i)
        # print(yaml_data.get(i))
        # print(yaml_data.get(i).get("value"))
        # list_data中添加参数值
        list_data.append((i, yaml_data.get(i).get("value")))
    return list_data


print(sys.path)
package_param_data()


class Test_Search(object):
    """
        def __init__(self):
            self.driver = init_hlj_driver()
        希望函数运行多次，但不希望每次运行都初始化和退出

    """

    # def __init__(self):
    #         self.driver = init_hlj_driver()
    #         sp = Search_Page(self.driver)
    #         sp.jump_guide()

    def setup_class(self):
        self.driver = init_hlj_driver()
        sp = Search_Page(self.driver)
        sp.jump_guide()

    @pytest.mark.parametrize('test_id, value', package_param_data())  # 参数传递三组参数，会运行三次
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("主页：设计搜索步骤001")
    def test_search(self, test_id, value):
        allure.attach('描述', '重复三次搜索步骤')

        # 实例化页面封装类
        sp = Search_Page(self.driver)
        # 调用操作类
        print("test_id:", test_id)
        sp.input_search_text(value)
        # self.driver.quit()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("主页：楼盘测试")
    def test_index_lp(self):
        assert 0

    def teardown_class(self):
        # 退出driver对象
        self.driver.quit()


if __name__ == "__main__":
    Test_Search().test_search(11, "H")
