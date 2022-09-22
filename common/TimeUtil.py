# -*- coding: utf-8 -*-
__author__ = "zt"

import time
from datetime import datetime, timedelta


class TimeUtil(object):
    DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        self.str_format_dict = {
            0: self.DEFAULT_FORMAT,
            1: "%Y-%m-%dT%H:%M:%SZ",
            2: "%Y-%m-%d %H:%M:%S.%f",
            3: "%Y-%m-%d %H:%M:%S.%f+00:00",
            4: "%Y-%m-%dT%H:%M:%S.%fZ",
        }

    def format(self, key=0):
        return self.str_format_dict[key]

    @staticmethod
    def stamp_int_now():
        """
        返回当前时间戳 int
        :return:  1657783485
        """
        return int(time.time())

    @staticmethod
    def stamp_float_now():
        """
        返回当前时间戳 float
        :return:  1657783502.8668659
        """
        return time.time()

    @staticmethod
    def datetime_now():
        """
        返回当前时间 datetime.datetime
        :return:  2022-07-14 15:25:19.267429
        """
        return datetime.now()

    @staticmethod
    def datetime_utc_now():
        """
        返回当前UTC时间 datetime.datetime
        :return:  2022-07-14 07:25:39.576659
        """
        return datetime.utcnow()

    @staticmethod
    def get_now_time(str_format=DEFAULT_FORMAT):
        """
        获取系统当前时间 %Y-%m-%d %H:%M:%S
        :return:  "2022-07-14 15:57:39"  <class 'str'>
        """
        return datetime.now().strftime(str_format)

    @staticmethod
    def str_to_datetime(str_data, str_format=DEFAULT_FORMAT):
        """
        字符串类型 转 datetime 类型
        :param str_data: "2022-07-14 15:25:54"
        :param str_format: 2022-07-14 15:25:54  <class 'datetime.datetime'>
        :return:
        """
        return datetime.strptime(str_data, str_format)

    @staticmethod
    def str_to_stamp(str_data, str_format=DEFAULT_FORMAT):
        """
        时间格式字符串 转 时间戳类型
        :param str_data:  "2022-07-14 15:25:54"
        :param str_format:  1657783554
        :return:
        """
        time_array = time.strptime(str_data, str_format)
        return int(time.mktime(time_array))

    @staticmethod
    def stamp_to_str(stamp_data, str_format=DEFAULT_FORMAT):
        """
        时间戳类型 转 字符串类型
        :param stamp_data:  1657783554
        :param str_format:  "2022-07-14 15:25:54"
        :return:
        """
        stamp_data = float(stamp_data)
        return time.strftime(str_format, time.localtime(stamp_data))

    @staticmethod
    def stamp_to_datetime(stamp_data):
        """
        时间戳类型 转 datetime类型
        :param stamp_data: 1657783554
        :return: datetime  2022-07-14 15:25:54  <class 'datetime.datetime'>
        """
        stamp_data = float(stamp_data)
        return datetime.fromtimestamp(stamp_data)

    @staticmethod
    def datetime_to_str(datetime_data, str_format=DEFAULT_FORMAT):
        """
        datetime类型 转 字符串类型
        :param datetime_data: 2022-07-14 15:25:54
        :param str_format: "2022-07-14 15:25:54"
        :return:
        """
        return datetime_data.strftime(str_format)

    @staticmethod
    def datetime_to_stamp(datetime_data):
        """
        datetime类型 转 时间戳类型
        :param datetime_data:
        :return:
        """
        return datetime_data.timestamp()

    @staticmethod
    def datetime_add(datetime_data, **args):
        """
        datetime时间类型 增加指定时间
        :param datetime_data:
        :param args:
        :return:
        """
        return datetime_data + timedelta(**args)

    @staticmethod
    def datetime_reduce(datetime_data, **args):
        """
        datetime时间类型 减少指定时间
        :param datetime_data:
        :param args:
        :return:
        """
        return datetime_data + timedelta(**args)

    @staticmethod
    def seconds_to_hours(seconds):
        """
        秒 转 小时
        :param seconds:
        :return:
        """
        hour = round(int(seconds) / 3600, 2)
        return hour

    @staticmethod
    def second_to_date(sec):
        """
        秒 转 时分秒
        :param sec:
        :return:
        """
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)

        return "{}:{}:{}".format(h, m, s)

    @staticmethod
    def getTimeDifference():
        """
        获取 当天零点 和 当天24点
        Returns:
            zero_today  2022-07-14 00:00:00
            last_today  2022-07-14 23:59:59
        """
        now = datetime.now()
        zero_today = now - timedelta(days=0, hours=now.hour, minutes=now.minute, seconds=now.second,
                                     microseconds=now.microsecond)
        last_today = zero_today + timedelta(hours=23, minutes=59, seconds=59)
        return zero_today, last_today
