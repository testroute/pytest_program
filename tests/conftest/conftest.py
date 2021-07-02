# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# """
# @File   :   conftest.py
# @Time   :   2021-06-08 23:13
# @Contact    :
# @Author     :   WG
# @Version    :   v 0.1
# @Desc  :
# """
import pytest

# 非特殊hook类fixture需要测试用例testcase（_test_two）形式调用fixture
# @pytest.fixture()
# def _test_two():
#     print("===================testtwo==============")
#
# 不支持类形式fixtures,但是可以在fixture方法中返回类，测试用例中再调用类方法。
# @pytest.fixture()
# class conftest():#不支持
#     @pytest.fixture()
#     def _set_token(self):
#         print("===================testone==============")
#         token = _get_token()

# 特殊hook类fixture不需要在测试用例处调用，系统会自动识别并调用
# 所有函数前调用
from common.CommonFuncs import _confirmLogin, _update_token_and_return, _read_param


def pytest_runtest_setup():
    print("pytest_runtest_setup")
    # token = _get_token()


# 扩展命令行参数
# def pytest_addoption(parser):
#     parser.addoption("--ip_type", action="store", default="loopback",
#                      help="ip type includes loopback, domain and local_network")

# 收集用例之后调用
# def pytest_collection_modifyitems():
#     print("===================pytest_collection_modifyitems==============")

@pytest.fixture()
def set_driver(request):
    class login_class():
        __token = _read_param('token')

        # class前执行一次
        def login_by_token(self):
            print("login by token")
            # if _confirmLogin(self.__token):
            #     js = 'window.localStorage.setItem("token","%s")' % self.__token
            #     cls.execute_script(script=js)
            # else:
            #     __token = _update_token_and_return()
            #     js = 'window.localStorage.setItem("token","%s")' % self.__token
            #     cls.execute_script(script=js)

        def login_by_cookie(self):
            print("login by cookie")
    if request.cls:
        request.cls.login_class = login_class()
        yield request.cls.login_class
    else:
        login_class = login_class()
        yield login_class
