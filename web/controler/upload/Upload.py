# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 15:55
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : Upload.py
# @Software: PyCharm
from flask import Blueprint,request,jsonify,redirect
from application import  app,db
from common.libs.UrlManager import UrlManager
import json, re
from common.libs.UploadService import UploadService
from common.models.model import Image

route_upload = Blueprint( 'upload_page',__name__ )

@route_upload.route( "/ueditor", methods = ['GET','POST'])
def ueditor():
    req = request.values
    action = req['action'] if 'action' in req else ''

    if action == "config":
        root_path = app.root_path
        config_path = "{0}/web/static/plugins/ueditor/upload_config.json".format(root_path)
        with open(config_path, encoding="utf-8") as fp:
            try:
                config_data = json.loads(re.sub(r'\/\*.*\*/', '', fp.read()))
            except:
                config_data = {}
        return jsonify(config_data)

    if action == "uploadimage":
        return uploadImage()

    if action == "listimage":
        return listImage()

    return "upload"


##上传功能
def uploadImage():
    resp = {"state":"SUCCESS","url":"","title":"","original":""}
    file_target = request.files
    upfile = file_target["upfile"] if "upfile" in file_target else None

    if upfile is None:
        resp["state"] = "上传失败"
        return jsonify(resp)

    ret = UploadService.uploadByFile(file=upfile)

    if ret["code"] != 200:
        resp["state"] = "上传失败" + ret["msg"]
        return jsonify(resp)

    resp['url'] = UrlManager.buildImgUrl(ret["data"]["file_key"])
    return jsonify(resp)

@route_upload.route("/pic",methods = [ "GET","POST" ])
def uploadPic():
	file_target = request.files
	upfile = file_target['pic'] if 'pic' in file_target else None
	callback_target = 'window.parent.upload'
	if upfile is None:
		return "<script type='text/javascript'>{0}.error('{1}')</script>".format( callback_target,"上传失败" )

	ret = UploadService.uploadByFile(upfile)
	if ret['code'] != 200:
		return "<script type='text/javascript'>{0}.error('{1}')</script>".format(callback_target, "上传失败：" + ret['msg'])

	return "<script type='text/javascript'>{0}.success('{1}')</script>".format(callback_target,ret['data']['file_key'] )


def listImage():
    resp = {"state": "SUCCESS", "list": [], "start": 0, "total": 0}

    req = request.values

    start = int(req["start"]) if "start" in req else 0
    page_size = int(req["page_size"]) if "page_size" in req else 20

    query = Image.query
    if start > 0:
        query = query.filter(Image.id < start)

    list = query.order_by(Image.id.desc()).limit(page_size).all()
    # list = query.order_by(Image.id.desc()).offset().limit(page_size).all()
    images = []
    if list:
        for item in list:
            images.append({"url":UrlManager.buildImgUrl(item.file_key)})

    resp["list"] = images
    resp["start"] = start
    resp["total"] = len(images)

    return jsonify(resp)