# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 22:54
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : manage.py
# @Software: PyCharm
import sys
from application import app,manager
from flask_script import Server
import traceback
import www

## Web server
manager.add_command("runserver", Server(host='127.0.0.1',port=app.config['SERVER_PORT'],use_debugger=True))

def main():
    manager.run()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
