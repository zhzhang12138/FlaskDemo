# -*- coding: utf-8 -*-
__author__ = "zt"

import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "fd98330dad85045242bd271ceb736681")

    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@host:port/db?charset=utf8mb4"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_TIMEOUT = 3000
    SQLALCHEMY_POOL_RECYCLE = 3000

    # 设置超时时间
    TIME_OUT = 100
