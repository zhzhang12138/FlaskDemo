# -*- coding: utf-8 -*-
from flask import request

from common.TimeUtil import TimeUtil
from models import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    remark = db.Column(db.Text, comment="备注")
    creator = db.Column(db.String(20))
    create_time = db.Column(db.DateTime)
    updator = db.Column(db.String(20))
    update_time = db.Column(db.DateTime)

    def save(self):
        """
        新增数据
        :return:
        """
        self.creator = request.user_id
        self.create_time = TimeUtil.get_now_time()
        self.updator = request.user_id
        self.update_time = TimeUtil.get_now_time()
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        更新数据
        :return:
        """
        self.updator = request.user_id
        self.update_time = TimeUtil.get_now_time()
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        """
        删除数据
        :return:
        """
        self.updator = request.user_id
        self.update_time = TimeUtil.get_now_time()
        db.session.delete(self)
        db.session.commit()

    def save_all(self, data):
        """
        保存多条数据
        :param data:
        :return:
        """
        db.session.execute(
            self.__table__.insert(),
            data
        )
        db.session.commit()
