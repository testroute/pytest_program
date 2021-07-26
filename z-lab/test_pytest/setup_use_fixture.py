#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   setup_use_fixture.py 
@Time   :   2021/7/12 15:57   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import pytest

from base.base_case import MyBaseCase
from common.CommonFuncs import _read_param, _confirmLogin, _update_token_and_return


@pytest.fixture(scope="session")
def set_driver(request):
    # __is_cls_request=__is_session_request = False

    class login_class:

        # class前执行一次
        def login_by_token(self, cls):
            print("login by token")
            __token = _read_param('token')
            cls.open("http://47.110.37.80:8088/#/")
            if _confirmLogin(__token):
                js = 'window.localStorage.setItem("token","%s")' % __token
                cls.execute_script(script=js)
            else:
                __token = _update_token_and_return()
                js = 'window.localStorage.setItem("token","%s")' % __token
                cls.execute_script(script=js)

        def login_by_cookie(self):
            print("login by cookie")
    # print("request.node:",request.node)
    # print( request.node.items[0].getparent(pytest.Class))
    # print( request.node.items[0].getparent(pytest.Class).obj)
    try: #测试类中返回
        #需要for循环
        request.node.items[0].getparent(pytest.Class).obj.login_class = login_class()
        # request.cls.login_class = login_class
        yield request.node.items[0].getparent(pytest.Class).obj.login_class
    except: #测试方法中返回
        login_class = login_class()
        yield login_class



class Test(MyBaseCase):
    @pytest.fixture(autouse=True)
    def setup_method_fixture(self, request, set_driver):
        self.login_class.login_by_token(self)
        self.method_name = request.function.__name__


    def test(self):
        assert self.method_name == 'test'
