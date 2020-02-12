# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 23:22
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : Helper.py
# @Software: PyCharm
from flask import g, render_template
import re,datetime

'''
密码强度验证
'''
def lenOK(pwd):
    if (len(pwd) >= 8):
        return True
    else:
        print("WARNING: The password should be at least 8 characters.")
        return False

def numberOK(pwd):
    pattern = re.compile('[0-9]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should include at least 1 number.")
        return False

def upperOK(pwd):
    pattern = re.compile('[A-Z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should include at least 1 upper character.")
        return False

def lowerOK(pwd):
    pattern = re.compile('[a-z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should include at least 1 lower character.")
        return False

def symbolOK(pwd):
    pattern = re.compile('^[a-z0-9A-Z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should start with numbers or characters.")
        return False

def checkpwd(pwd):
    return lenOK(pwd) and numberOK(pwd) and upperOK(pwd) and lowerOK(pwd) and symbolOK(pwd)

'''
自定义分页类
'''
def iPagination( params ):
    import math

    ret = {
        "is_prev":1,
        "is_next":1,
        "from" :0 ,
        "end":0,
        "current":0,
        "total_pages":0,
        "page_size" : 0,
        "total" : 0,
        "url":params['url']
    }

    total = int( params['total'] )
    page_size = int( params['page_size'] )
    page = int( params['page'] )
    display = int( params['display'] )

    total_pages = int( math.ceil( total / page_size ) )
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int( math.ceil( display / 2 ) )

    if page - semi > 0 :
        ret['from'] = page - semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages :
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range( ret['from'],ret['end'] + 1 )
    return ret
'''
统一渲染方法
'''

def ops_render(template, context = {}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)

'''
获取当前时间
'''
def getCurrentDate(format = '%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(format)