# -*- coding: utf-8 -*-
__author__ = "zt"

from enum import Enum


class BaseEnm(Enum):
    def getCode(self):
        """根据枚举名称取状态码code

        @return: 状态码code
       """
        return self.value[0]

    def getMessage(self):
        """根据枚举名称取状态说明message

        @return: 状态说明message
        """
        return self.value[1]


class ErrorCodeEnm(BaseEnm):
    """
    ErrorCode信息
    """
    SUCCESS = (0, 'SUCCESS')
    ERROR_1001 = (1001, '参数错误')
    ERROR_1002 = (1002, '公司类型不能为空')
    ERROR_1003 = (1003, '客户已存在,请勿重复添加')
    ERROR_1004 = (1004, '客户不存在,请检查参数是否正确')
