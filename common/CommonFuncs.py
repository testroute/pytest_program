#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   CommonFuncs.py 
@Time   :   2021/6/7 20:13   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import sys
import traceback

import requests
import yaml


def __getToken():
    """
    获取网站token
    :return:token字符串
    """
    url = "http://stuq.ceshiren.com:8089/user/login"
    body = {
        "password": "123",
        "userName": "wg123"
    }
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json",
        "token": "1"
    }
    res = requests.post(url, json=body, headers=headers)
    _token = res.json()["data"]["token"]
    return _token


# curl -X GET "http://stuq.ceshiren.com:8089/user/isLogin" -H  "accept: */*" -H  "token:
# 3e167c28e2f2b962bf6e9c80543470e6"
def _confirmLogin(token):
    """
    检查登录状态
    :param token:登录token
    :return: 布尔类型，是否登录
    """
    url = "http://stuq.ceshiren.com:8089/user/isLogin"
    headers = {
        "accept": "*/*",
        "token": token
    }
    res = requests.get(url, headers=headers)
    # print(res.json())
    if res.json()["message"] == "成功":
        return True
    else:
        return False


def read_yaml(file):
    """
    读取文件，返回字典型内容
    :param file: 字符串，文件路径
    :return: 字典型文件内容
    """
    with open(file, "r+", encoding="utf-8") as f:
        datas = yaml.safe_load(f.read())
        f.close()
    # print(datas)
    return datas


def _update_token_and_return():
    """
    获取新token写入文件并返回
    :return:更新后的token串
    """
    datas = read_yaml("../datas/common_datas.yaml")
    with open("../datas/common_datas.yaml", "w+", encoding="utf-8") as f:
        token = __getToken()
        try:
            datas["token"] = token
            yaml.safe_dump(datas, f)
            f.close()
            return datas["token"]
        except Exception as e:
            f.close()
            raise e


def _read_param(attr):
    """
    读取token
    :param attr 读取内容的关键字
    :return: 对应内容
    """
    datas = read_yaml("../datas/common_datas.yaml")
    try:
        return datas[attr]
    except Exception as e:
        # traceback.print_exc()
        raise e


if __name__ == '__main__':
    print(_read_param("token"))
    print(_update_token_and_return())
