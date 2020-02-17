# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 22:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : base_setting.py
# @Software: PyCharm
import os
SERVER_PORT = 8888
DEBUG = True
SQLALCHEMY_ECHO = True
# SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.89.77/wechatapp'
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/wechatapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = 'UTF-8'
AUTH_COOKIE_NAME = 'make-love'
##过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico",
]

PAGE_SIZE = 5
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"删除"
}

MINA_APP = {
    "appid":"wx48042d027db8f02c",
    "appkey":"a832465654894774a99387bf1aa001ef",
}

APP = {
    "domain": "http://127.0.0.1:8888"
}

UPLOAD = {
    "ext":["jpg","gif","bmp","jpeg","png"],
    "prefix_path": "\\web\\static\\upload\\",
    "prefix_url":"\\static\\upload\\"
}


