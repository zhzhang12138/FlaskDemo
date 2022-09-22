# -*- coding: utf-8 -*-
__author__ = "zt"

from flask import Blueprint
from flask_restful import Api
from sources.web.WebAPI import HealthExamination, LoginAPI

new_web_api_blueprint = Blueprint("new_web_api", __name__, url_prefix="/web")
new_web_api = Api(app=new_web_api_blueprint)

# 健康检查
new_web_api.add_resource(HealthExamination, "/health")
# 登录
new_web_api.add_resource(LoginAPI, "/login")
