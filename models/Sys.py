# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, DateTime, FetchedValue, BigInteger
from models.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    company_type = Column(String(20), nullable=False)
    nickname = Column(String(30), nullable=False)
    user_name = Column(String(30), nullable=False)
    user_type = Column(Integer, server_default=FetchedValue())
    email = Column(String(50))
    phone = Column(String(20))
    sex = Column(Integer)
    avatar = Column(String(100))
    password = Column(String(50), nullable=False)
    dept_id = Column(BigInteger)
    del_flag = Column(Integer, server_default=FetchedValue())
    login_ip = Column(String(50))
    login_date = Column(DateTime)
    status = Column(Integer, nullable=False, server_default=FetchedValue())

    def check_password(self, passwd):
        """
        检查密码
        :param passwd:
        :return: 0/1
        """
        if self.password == passwd:
            return 1
        else:
            return 0
