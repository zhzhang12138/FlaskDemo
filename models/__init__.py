# -*- coding: utf-8 -*-
__author__ = "zt"

from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def request2model(module_path: str, module_name: str, class_name: str, attr_json: dict, alias_map=None):
    if alias_map is None:
        alias_map = dict()

    model_module = __import__(f"{module_path}.{module_name}")
    m_py = getattr(model_module, module_name)
    obj_class_name = getattr(m_py, class_name)
    obj = obj_class_name()
    for key, value in attr_json.items():
        setattr(obj, alias_map.get(key, key), value)

    return obj


def request2model_list(module_path: str, module_name: str, class_name: str, attr_json_list: list, alias_map=None):
    if alias_map is None:
        alias_map = dict()

    model_module = __import__(f"{module_path}.{module_name}")
    m_py = getattr(model_module, module_name)
    obj_class_name = getattr(m_py, class_name)
    obj_list = []
    for attr_json in attr_json_list:
        obj = obj_class_name()
        for key, value in attr_json.items():
            setattr(obj, alias_map.get(key, key), value)
        obj_list.append(obj)
    return obj_list


def model2json(obj: object):
    data = {}
    for c in obj.__table__.columns:
        type_class_str = c.type.__str__()
        if type_class_str == "BIGINT":
            data[c.name] = getattr(obj, c.name, 0)
            continue
        elif c.name in ["password", "token"]:
            continue
        elif type_class_str in ["INTEGER"]:
            val = getattr(obj, c.name, None)
            if val is not None:
                data[c.name] = val
            else:
                data[c.name] = 0
        elif type_class_str in ["FLOAT"]:
            val = getattr(obj, c.name, None)
            if val is not None:
                data[c.name] = float(val)
            else:
                data[c.name] = float(0)
        elif type_class_str in ["TIMESTAMP"]:
            val = getattr(obj, c.name, None)
            if val is not None:
                data[c.name] = int(val.timestamp() * 1000)
            else:
                data[c.name] = 0
        elif type_class_str in ["DATETIME", "DATE", "DateTime", "Date"]:
            val = getattr(obj, c.name, None)
            if val is not None:
                data[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                data[c.name] = ""
            continue
        elif type_class_str in ["TIME"]:
            val = getattr(obj, c.name, None)
            if val is not None:
                data[c.name] = val.strftime("%H:%M:%S")
            else:
                data[c.name] = ""
            continue
        elif not getattr(obj, c.name, ""):
            data[c.name] = ""
        else:
            data[c.name] = getattr(obj, c.name, getattr(obj, c.name, ""))
    if getattr(obj, "wechat_username", None) and "wechat_username" not in obj.__table__.columns:
        data["wechat_username"] = getattr(obj, "wechat_username")
    relationships = obj.__mapper__.relationships.keys()
    if relationships:
        for key in relationships:
            is_list = obj.__mapper__.relationships[key].uselist
            data[key] = list()
            if not is_list:
                items = getattr(obj, key)
                if items:
                    dict_out = dict()
                    dict_relationship = items.__dict__
                    for k, v in dict_relationship.items():
                        if not k[0] == "_":
                            if isinstance(v, datetime) or isinstance(v, date):
                                dict_out[k] = v.strftime("%Y-%m-%d %H:%M:%S")
                            elif k in ["password"]:
                                continue
                            elif not v:
                                dict_out[k] = ""
                            else:
                                dict_out[k] = v
                    data[key].append(dict_out)
                else:
                    data[key].append(dict())
            else:
                items = getattr(obj, key)
                for item in items:
                    dict_out = dict()
                    dict_relationship = item.__dict__
                    for k, v in dict_relationship.items():
                        if not k[0] == "_":
                            if isinstance(v, datetime) or isinstance(v, date):
                                dict_out[k] = v.strftime("%Y-%m-%d %H:%M:%S")
                            elif k in ["password"]:
                                continue
                            elif not v:
                                dict_out[k] = ""
                            else:
                                dict_out[k] = v
                    data[key].append(dict_out)
    return data


def model2json_list(obj_list: list):
    data_list = []
    for obj in obj_list:
        data = model2json(obj=obj)
        data_list.append(data)
    return data_list
