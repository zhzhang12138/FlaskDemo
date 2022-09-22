# -*- coding: utf-8 -*-
__author__ = "zt"

from flask import Flask
from flask_cors import CORS

from settings import Config
from models import db
from sources import before_request
from sources.web import new_web_api_blueprint


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)
    db.init_app(app=app)

    app.before_request(before_request)

    CORS(app=app)
    app.register_blueprint(new_web_api_blueprint)
    return app
