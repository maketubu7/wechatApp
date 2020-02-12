# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 23:34
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : index.py
# @Software: PyCharm
from flask import Blueprint,g
from common.libs.Helper import ops_render

route_index = Blueprint('/',__name__)
@route_index.route('/')
def index():
    return ops_render("index/index.html")