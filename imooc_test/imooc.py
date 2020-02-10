# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 21:26
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : imooc.py
# @Software: PyCharm
from flask import Blueprint

#路由设置
route_imooc = Blueprint("imooc_page",__name__)

@route_imooc.route('/')
def index():
    return 'imooc index page'

@route_imooc.route('/hello')
def hello():
    return 'imooc hello world'






if __name__ == "__main__":
    pass