# -*- coding: utf-8 -*-
import pickle
import redis
from settings import Config


class Redis(object):
    """
    redis数据库操作
    """

    @staticmethod
    def _get_r():
        host = Config.REDIS_HOST
        port = Config.REDIS_PORT
        db = Config.REDIS_DB
        passwd = Config.REDIS_PASSWD
        r = redis.StrictRedis(host=host, port=port, db=db, password=passwd)
        return r

    @classmethod
    def write(cls, key, value, expire=None):
        """
        写入键值对
        """
        # 判断是否有过期时间，没有就设置默认值
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = Config.REDIS_EXPIRE
        r = cls._get_r()
        r.set(key, value, ex=expire_in_seconds)

    @classmethod
    def write_dict(cls, key, value, expire=None):
        """
        将内存数据二进制通过序列号转为文本流，再存入redis
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = Config.REDIS_EXPIRE
        r = cls._get_r()
        r.set(pickle.dumps(key), pickle.dumps(value), ex=expire_in_seconds)

    @classmethod
    def read_dict(cls, key):
        """
        将文本流从redis中读取并反序列化，返回
        """
        r = cls._get_r()
        data = r.get(pickle.dumps(key))
        if data is None:
            return None
        return pickle.loads(data)

    @classmethod
    def read(cls, key):
        """
        读取键值对内容
        """
        r = cls._get_r()
        value = r.get(key)
        return value.decode('utf-8') if value else value

    @classmethod
    def hset(cls, name, key, value):
        """
        写入hash表
        """
        r = cls._get_r()
        r.hset(name, key, value)

    @classmethod
    def hmset(cls, key, *value):
        """
        读取指定hash表的所有给定字段的值
        """
        r = cls._get_r()
        value = r.hmset(key, *value)
        return value

    @classmethod
    def hget(cls, name, key):
        """
        读取指定hash表的键值
        """
        r = cls._get_r()
        value = r.hget(name, key)
        return value.decode('utf-8') if value else value

    @classmethod
    def hgetall(cls, name):
        """
        获取指定hash表所有的值
        """
        r = cls._get_r()
        return r.hgetall(name)

    @classmethod
    def delete(cls, *names):
        """
        删除一个或者多个
        """
        r = cls._get_r()
        r.delete(*names)

    @classmethod
    def hdel(cls, name, key):
        """
        删除指定hash表的键值
        """
        r = cls._get_r()
        r.hdel(name, key)

    @classmethod
    def expire(cls, name, expire=None):
        """
        设置过期时间
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = Config.REDIS_EXPIRE
        r = cls._get_r()
        r.expire(name, expire_in_seconds)
