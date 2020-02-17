# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 9:58
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : Member.py
# @Software: PyCharm
from flask import Blueprint,request,jsonify,redirect
from common.libs.Helper import ops_render,iPagination,getCurrentDate
from common.libs.UrlManager import UrlManager
from common.models.model import Member
from application import app,db

route_member = Blueprint("member_page", __name__)

@route_member.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req["p"]) if ("p" in req and req["p"]) else 1
    page_size = app.config["PAGE_SIZE"]
    query = Member.query

    if "mix_kw" in req:
        query = query.filter(Member.nickname.ilike("%{}%".format(req["mix_kw"])))

    if "status" in req and int(req["status"]) > -1:
        query = query.filter(Member.status == int(req["status"]))

    page_params = {
        "total": query.count(),
        "page_size": page_size,
        "page":page,
        "display": app.config["PAGE_DISPLAY"],
        "url": request.full_path.replace("&p={}".format(page),"")
    }

    pages = iPagination( page_params )
    offset = (page - 1) * page_size
    list = query.order_by(Member.id.desc()).offset(offset).limit(page_size).all()

    resp_data["list"] = list
    resp_data["pages"] = pages
    resp_data["search_con"] = req
    resp_data["current"] = 'index'
    resp_data["status_mapping"] = app.config["STATUS_MAPPING"]

    return ops_render("/member/index.html",resp_data)

@route_member.route("/set",methods=["GET","POST"])
def set():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get("id", 0))
        reback_url = UrlManager.buildUrl("/member/index")
        if id < 1:
            return redirect(reback_url)

        info = Member.query.filter_by(id=id).first()
        if not info:
            return redirect(reback_url)

        if info.status != 1:
            return redirect(reback_url)

        resp_data['info'] = info
        resp_data['current'] = 'index'
        return ops_render("member/set.html", resp_data)

    resp = {"code": 200, "msg": "操作成功", "data": {}}
    req = request.values
    id = req["id"] if "id" in req else 0
    nickname = req["nickname"] if "nickname" in req else ""

    if not nickname or len(nickname) < 1:
        resp["code"] = -1
        resp["msg"] = "请输入正确的名称~~"
        return jsonify(resp)

    info = Member.query.filter_by(id=id).first()
    info.nickname = nickname
    db.session.add(info)
    db.session.commit()
    return jsonify(resp)

@route_member.route("/comment",methods=["GET","POST"])
def comment():
    pass

@route_member.route("/ops",methods=["GET","POST"])
def ops():

    req = request.values
    resp = {"code":200,"msg":"操作成功~~","data":{}}

    id = int(req["id"]) if "id" in req else 0
    act = req["act"] if "act" in req else ""

    if id < 1:
        resp["code"] = -1
        resp["msg"] = "指定账号不存在"
        return jsonify(resp)

    if act not in ["remove","recover"]:
        resp["code"] = -1
        resp["msg"] = "无效操作"
        return jsonify(resp)

    member_info = Member.query.filter_by(id = id).first()

    if not member_info:
        resp["code"] = -1
        resp["msg"] = "指定账号不存在"
        return jsonify(resp)

    if act == "remove":
        member_info.status = 0
    else:
        member_info.status = 1

    member_info.updated_time = getCurrentDate()
    db.session.add(member_info)
    db.session.commit()

    return jsonify(resp)



