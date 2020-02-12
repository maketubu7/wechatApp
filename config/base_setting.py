# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 22:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : base_setting.py
# @Software: PyCharm
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
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico",
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10