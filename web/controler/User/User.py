# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 11:44
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : User.py
# @Software: PyCharm
from flask import Blueprint,request, jsonify, make_response,redirect,g
import json
from common.libs.user.UserService import UserService
from common.models.model import User
from application import app,db
from common.libs.UserManager import UrlManager
from common.libs.Helper import ops_render,checkpwd

route_user = Blueprint('user_page',__name__)

@route_user.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return ops_render("user/login.html")

    resp = {'code':200,'msg':'登录成功','data':{}}
    req = request.values
    login_name = req["login_name"] if 'login_name' in req else ''
    login_pwd = req["login_pwd"] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1 :
        resp["code"] = -1
        resp["msg"] = '请输入正确的用户名'
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1 :
        resp["code"] = -1
        resp["msg"] = '请输入正确的密码！！'
        return jsonify(resp)

    user_info = User.query.filter_by(login_name = login_name).first()
    if not user_info:
        resp["code"] = -1
        resp["msg"] = '请输入正确的用户名密码！！-1'
        return jsonify(resp)

    if user_info.login_pwd != UserService.genPwd(login_pwd, user_info.login_salt):
        app.logger.info(UserService.genPwd(login_pwd, user_info.login_salt))
        resp["code"] = -1
        resp["msg"] = '请输入正确的用户名密码！！-2'
        return jsonify(resp)
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config["AUTH_COOKIE_NAME"],"%s#%s"%(UserService.geneAuthCode(user_info),user_info.uid),60*60*24)
    return response

@route_user.route('/edit',methods = ["GET","POST"])
def edit():
    if request.method == "GET":
        return ops_render("user/edit.html",{"current":"edit"})

    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values
    nickname = req["nickname"] if "nickname" in req else ""
    email = req["email"] if "email" in req else ""

    if nickname is None or len(nickname) < 2:
        resp["code"] = -1
        resp["msg"] = "请输入符合规范的姓名"
        return jsonify(resp)

    if email is None or len(email) < 2:
        resp["code"] = -1
        resp["msg"] = "请输入符合规范的邮箱"
        return jsonify(resp)

    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add( user_info )
    db.session.commit()
    return jsonify(resp)

@route_user.route('/reset-pwd',methods = ["GET","POST"])
def resetPwd():
    if request.method == 'GET':
        return ops_render("user/reset_pwd.html",{"current":"reset-pwd"})

    req = request.values
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    old_password = req["old_password"] if "old_password" in req else ""
    new_password = req["new_password"] if "new_password" in req else ""

    if old_password is None or len(old_password) < 6:
        resp["code"] = -1
        resp["msg"] = "请输入合法的验证密码！"
        return jsonify(resp)

    if new_password is None or not checkpwd(new_password):
        resp["code"] = -1
        resp["msg"] = "请输入合法的新密码（包含大小写与数字）！"
        return jsonify(resp)

    if new_password == old_password:
        resp["code"] = -1
        resp["msg"] = "新密码不能与旧密码相同！"
        return jsonify(resp)

    user_info = g.current_user
    app.logger.info(user_info.login_pwd)
    app.logger.info(UserService.genPwd(old_password,user_info.login_salt))
    app.logger.info(UserService.genPwd('234567',user_info.login_salt))
    app.logger.info(old_password)

    if user_info.login_pwd != UserService.genPwd(old_password,user_info.login_salt):
        resp["code"] = -1
        resp["msg"] = "请输入正确的密码！"
        return jsonify(resp)

    ##设置新密码,并进行
    if checkpwd(new_password):
        user_info.login_pwd = UserService.genPwd(new_password,user_info.login_salt)
        app.logger.info(user_info.login_pwd)
        ##提交新密码
        db.session.add(user_info)
        db.session.commit()
        response = make_response(json.dumps(resp))

        ##更新cookie，保持登录
        response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (UserService.geneAuthCode(user_info), user_info.uid),
                            60 *60 * 24 * 120)

        return response

@route_user.route("/logout")
def logout():
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))
    response.delete_cookie(app.config["AUTH_COOKIE_NAME"])
    return response


