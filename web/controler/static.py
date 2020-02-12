# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 12:24
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : static.py
# @Software: PyCharm
from flask import Blueprint, send_from_directory
from application import app

route_static = Blueprint('static',__name__)

@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path+"/web/static/", filename)