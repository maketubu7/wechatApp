# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 22:56
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : www.py
# @Software: PyCharm

"""
拦截器
"""
from web.interceptors.AuthInterceptor import *


from web.controler.index import route_index
from web.controler.User.User import route_user
from web.controler.account.Account import route_account
from web.controler.static import route_static
from application import app

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_account,url_prefix='/account')