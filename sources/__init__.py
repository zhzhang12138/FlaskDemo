# -*- coding: utf-8 -*-
__author__ = "zt"

from flask import request
from sqlalchemy import and_

from common.JwtUtil import decode_auth_token
from common.RedisUtil import Redis
from common.ResponseUtil import ResponseUtil
from common.Constant import MANAGER_EXCLUDE_URL_PATH
from config.ErrorCode import ErrorCodeEnm
from models.Sys import User


def before_request():
    auth_token = request.headers.get("Authorization", None)

    # 免验签接口
    if request.path in MANAGER_EXCLUDE_URL_PATH:
        return

    # token不存在 且 是免验签接口 则通过
    if auth_token is None and request.path in MANAGER_EXCLUDE_URL_PATH:
        return

    # token不存在 且 不是免验签接口 则报错
    if auth_token is None and request.path not in MANAGER_EXCLUDE_URL_PATH:
        return ResponseUtil.output_json(result={}, code=ErrorCodeEnm.ERROR_1001.getCode(),
                                        msg=ErrorCodeEnm.ERROR_1001.getMessage())

    user_info = decode_auth_token(auth_token)

    if not user_info:
        return ResponseUtil.output_json(result={}, code=ErrorCodeEnm.ERROR_1001.getCode(),
                                        msg=ErrorCodeEnm.ERROR_1001.getMessage())
    user_id = user_info.get('sub', '')

    if not user_id:
        return ResponseUtil.output_json(result={}, code=ErrorCodeEnm.ERROR_1001.getCode(),
                                        msg=ErrorCodeEnm.ERROR_1001.getMessage())

    user = User.query.filter(and_(User.status == 1, User.id == user_id)).first()

    if not user:
        return ResponseUtil.output_json(result={}, code=ErrorCodeEnm.ERROR_1001.getCode(),
                                        msg=ErrorCodeEnm.ERROR_1001.getMessage())

    key = f"token_{user.company_type}_{user_id}"
    redis_token = Redis.read(key)

    if not redis_token:
        return ResponseUtil.output_json(result={}, code=ErrorCodeEnm.ERROR_1001.getCode(),
                                        msg=ErrorCodeEnm.ERROR_1001.getMessage())

    if auth_token != redis_token:
        return ResponseUtil.output_json(result={}, code=ErrorCodeEnm.ERROR_1001.getCode(),
                                        msg=ErrorCodeEnm.ERROR_1001.getMessage())

    setattr(request, "user_id", str(user.id))
    setattr(request, "user_name", user.user_name)
    setattr(request, "company_type", user.company_type)
