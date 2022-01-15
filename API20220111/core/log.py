# _*_ coding: utf-8 _*_
# _author_: Lingl
# 2022/1/11

import logging


class Log:
    def __init__(self, level="DEBUG"):
        # 日志器对象
        self.log = logging.getLogger('llylog')
        self.log.setLevel(level)


