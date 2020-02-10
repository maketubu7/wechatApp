# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 21:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : lib.py
# @Software: PyCharm

class UrlManager(object):
    @staticmethod
    def BuildUrl(path):
        return path

    @staticmethod
    def BuildStaticUrl(path):
        path = path + '?version=%s'%'2019'
        return UrlManager.BuildUrl(path)


if __name__ == "__main__":
    pass