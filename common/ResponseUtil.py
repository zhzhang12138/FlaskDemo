# -*- coding: utf-8 -*-
__author__ = "zt"

import json
from flask_restful import Api
from flask import make_response, Response


api = Api()


class ResponseUtil(object):

    @staticmethod
    @api.representation("application/json")
    def output_json(result: dict, code=0, http_status_code=200, headers=None, msg=None) -> Response:
        """
        封装Response返回体

        :param msg:
        :param http_status_code:
        :param result:
        :param code: HTTP 状态码
        :param headers: HTTP头部信息
        :return:

        """

        response_data = {
            "code": code,
            "msg": msg,
            "data": result
        }
        resp = make_response(json.dumps(response_data), http_status_code)
        resp.mimetype = "application/json"
        resp.headers.extend(headers or {})
        return resp
