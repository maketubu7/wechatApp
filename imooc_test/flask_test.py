# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 20:40
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : flask_test.py
# @Software: PyCharm
'''
每次发版都会有一个版本号

'''
import sys
from flask import Flask
from wechatApp.imooc_test.imooc import route_imooc
from wechatApp.commonLib.lib  import UrlManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 引入其他的路由
app.register_blueprint(route_imooc, url_prefix= '/imooc')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.89.77/wechatApp'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@172.0.0.1/wechatApp'
db = SQLAlchemy(app)


@app.route('/')
def run():
    url1 = UrlManager.BuildUrl('/api')
    url2 = UrlManager.BuildStaticUrl('/api')
    msg = 'hello world %s %s'%(url1, url2)
    app.logger.info(msg)
    app.logger.error(msg)
    return msg

@app.route('/hello')
def hello():
    from sqlalchemy import text
    sql = text("select * from `user`")
    result = db.engine.execute(sql)
    for item in result:
        app.logger.info(item)
    return 'sql'
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return 'This page does not exists', 404



if __name__ == "__main__":
    app.run(host='192.168.89.1',port=8888,debug=True)