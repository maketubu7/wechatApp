# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 21:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : UrlManager.py
# @Software: PyCharm
import re
from application import app

class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod  ##静态资源加载目录
    def buildStaticUrl(path):
        path = "/static"+path + '?version=%s'%'2019'
        return UrlManager.buildUrl(path)

    @staticmethod  ##上传图片资源加载
    def buildImgUrl(path):
        app_config = app.config["APP"]
        url = app_config["domain"] + app.config["UPLOAD"]["prefix_url"] + path
        return url



if __name__ == "__main__":
    pass