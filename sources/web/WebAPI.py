# -*- coding: utf-8 -*-
__author__ = "zt"

from flask import request
from flask_restful import Resource

from common.JwtUtil import encode_auth_token
from common.ResponseUtil import ResponseUtil
from config.ErrorCode import ErrorCodeEnm


class HealthExamination(Resource):
    def get(self):
        """
        健康检查
        :return:
        """
        return ResponseUtil.output_json(result={}, msg=ErrorCodeEnm.SUCCESS.getMessage(),
                                        code=ErrorCodeEnm.SUCCESS.getCode())


class LoginAPI(Resource):
    def post(self):
        """
        登录
        :return:
        """
        data = request.get_json()

        token = str(encode_auth_token(12138, 12138), encoding="UTF-8")

        result_map = {
            "token": token,
        }

        return ResponseUtil.output_json(msg=ErrorCodeEnm.SUCCESS.getMessage(), result=result_map,
                                        code=ErrorCodeEnm.SUCCESS.getCode())
