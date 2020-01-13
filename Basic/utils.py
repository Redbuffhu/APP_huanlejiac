import logging, os


class Logbuilder(object):
    def __init__(self, loggername='log', loglevel=None):
        self.loggername = loggername

    def get_consolehandler(self, formatter):
        # 创建一个handler，添加handler用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        return console_handler

    def getlog(self):
        # 创建一个logger
        self.logger = logging.getLogger(self.loggername)
        self.logger.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('\n%(message)s', "%Y-%m-%d %H:%M:%S")
        console_handler = self.get_consolehandler(formatter)
        self.logger.addHandler(console_handler)

        return self.logger


log = Logbuilder('log:').getlog()
