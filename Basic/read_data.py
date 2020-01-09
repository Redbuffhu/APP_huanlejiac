# -*- coding=utf-8 -*-
# 数据解析读取方法

import yaml
import os


class Read_Data(object):
    def __init__(self, file_name):
        """
            使用pytest运行在项目的根目录下运行，即App_Project目录
            期望路径为：香炉虽在目录/App——Project/Data/file_name
            :param file_name:
        """
        self.file_path = os.getcwd() + os.sep + 'Data' + os.sep + file_name

    def return_data(self):
        with open(self.file_path, 'r', encoding='UTF-8',  errors='ignore') as f:
            data = yaml.safe_load(f)
            return data




