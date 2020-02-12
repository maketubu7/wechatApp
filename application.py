# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 22:54
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : application.py.py
# @Software: PyCharm
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask import Flask
import os
from common.libs.UserManager import UrlManager

class Application(Flask):
    def __init__(self, import_name,template_folder=None,root_path = None):
        super(Application,self)\
            .__init__(import_name,template_folder=template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__,template_folder=os.getcwd() + "/web/templates",root_path=os.getcwd())
manager = Manager(app)


'''
向html中注入我们的通用方法,函数模板
'''
app.add_template_global(UrlManager.buildUrl,"buildUrl")
app.add_template_global(UrlManager.buildStaticUrl,"buildStaticUrl")