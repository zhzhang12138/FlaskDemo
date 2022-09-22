# -*- coding: utf-8 -*-
__author__ = "zt"

from sqlalchemy import or_, and_


def get_and_like_query(like):
    """
    模糊查询 AND
    :param like:
    :return:
    """
    if len(like) < 1:
        like = or_(*[])
    elif len(like) == 1:
        like = like[0]
    else:
        like = and_(*like)

    return like
