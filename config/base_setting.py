# -*- coding: utf-8 -*-
SERVER_PORT = 8888
SQLALCHEMY_ECHO = False
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/wechatapp?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

AUTH_COOKIE_NAME = "mooc_food"
SEO_TITLE = "make love"
##过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wx48042d027db8f02c',
    'appkey':'62b1952f506f24710f2bb6afad910bb9',
    'paykey':'xxxxxxxxxxxxxx换自己的',
    'mch_id':'xxxxxxxxxxxx换自己的',
    'callback_url':'/api/order/callback'
}


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'\\web\\static\\upload\\',
    'prefix_url':'\\static\\upload\\'
}

APP = {
    'domain':'http://127.0.0.1:8888'
}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}