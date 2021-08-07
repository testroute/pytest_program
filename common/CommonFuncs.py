#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   CommonFuncs.py 
@Time   :   2021/6/7 20:13   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   通用方法类,通过request，read yaml获取基本数据，以及提供通用方法供其他模块调用
"""
import configparser
import os
import requests
import yaml
from base.db import session
from base.models.test_case import TestCase


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
    file_path = os.path.dirname(__file__).strip("common").__add__("datas\\common_datas.yaml")
    read_datas = read_yaml(file_path)
    datas = read_datas if read_datas else {"token":""}
    print("datas:",datas)
    with open(file_path, "w+", encoding="utf-8") as f:
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

    file_path = os.path.dirname(__file__).strip("common").__add__("datas\\common_datas.yaml")
    datas = read_yaml(file_path)
    try:
        return datas[attr]
    except Exception as e:
        # traceback.print_exc()
        raise e

def _read_url(attr):
    """
    读取token
    :param attr 读取内容的关键字
    :return: 对应内容
    """

    file_path = os.path.dirname(__file__).strip("common").__add__("config\\config.ini")
    config = configparser.ConfigParser()
    config.read(file_path)
    try:
        return config.get(attr,"base_url")
    except Exception as e:
        # traceback.print_exc()
        raise e


def _confirm_scope(request):
    """
    判断fixture的作用范围
    :param request:
    :return: bool
    """
    scope = None
    try:
        if request.function:
            scope = request.function
    except Exception as e:
        print("请确认fixture的作用范围")
        raise e

    return scope

def data_prepare(testcase:str):
    """
    使用sqlalchemy,针对测试用例名实现数据清洗
    :param testcase: 测试用例名
    :return: None
    """
    if testcase.__contains__("test_add_test"):
        datas = get_test_datas("TestTestcasePage.yaml","test_add_test")
        casenames = ["正常标题1"]
        casedatas = ["数字标题描述"]
        # for casename in datas:
        #     casenames.append(str(casename[1]))
        #     casedatas.append(str(casename[2]))
        print(f"casenames:{casenames};casedatas:{casedatas}")
        session.query(TestCase).filter(TestCase.case_name.in_(casenames),TestCase.case_data.in_(casedatas)).delete(synchronize_session=False)
        # 删除TestCase表中的数据，使用synchronize_session异步删除多条数据
        session.close()
    else:
        pass
def get_test_datas(filename,casename):
    """
    获取针对测试类的参数化文件内容
    :param filename:测试类对应配置文件
    :param casename: 测试用例名
    :return: 参数化数据列表
    """
    # 打开文件
    file = os.path.dirname(__file__).strip("common").__add__(f"testcases\\parameterized_datas\\{filename}")
    # print(file)
    with open(file,encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # 获取文件中key为datas的数据
        add_datas = datas[casename]
        # print("add_datas:",datas)
    f.close()
    return add_datas

if __name__ == '__main__':
    # datas = get_test_datas("TestTestcasePage.yaml","test_add_test")
    # datas = _update_token_and_return()
    data_prepare("test_add_test")
