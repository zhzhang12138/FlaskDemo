# -*- coding: utf-8 -*-
__author__ = "zt"

from datetime import datetime, timedelta

import jwt

from settings import Config


def encode_auth_token(user_id, time_token=1):
    """
    生成token
    :param user_id:
    :param time_token:
    :return:
    """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=time_token),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            Config.SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    解密token
    :param auth_token:
    :return:
    """
    try:
        payload = jwt.decode(auth_token, Config.SECRET_KEY, algorithm='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
