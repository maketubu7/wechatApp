# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 14:59
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

route_api = Blueprint('api_page',__name__)
from web.controler.api.Member import *
@route_api.route("/")
def index():
    return 'mina'