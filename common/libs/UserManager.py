# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 21:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : UserManager.py
# @Software: PyCharm
import re

class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = "/static"+path + '?version=%s'%'2019'
        return UrlManager.buildUrl(path)


if __name__ == "__main__":
    pass