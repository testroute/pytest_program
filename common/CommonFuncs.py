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
    url = "http://stuq.ceshiren.com:8089/user/login"
    headers = {
        "accept": "*/*",
        "token": token
    }
    res = requests.get(url, headers=headers)
    if res.json()["message"] == "成功":
        return True
    else:
        return False


def _updateToken():

    with open("../datas/common_datas.yaml","w+") as f:
        data = yaml.safe_load(f)
        token = __getToken()
        f.write(token)
        f.close()


def _readToken():
    with open("../datas/common_datas.yaml","r+",encoding="utf-8") as f:
        data = yaml.safe_load(f)
        Token = data["token"]
        f.close()