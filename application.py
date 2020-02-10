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

class Application(Flask):
    def __init__(self, import_name):
        super(Application,self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)



class Demo(object):
    pass


if __name__ == "__main__":
    pass