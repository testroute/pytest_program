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
# import pytest
# import seleniumbase
# import requests
#
#非特殊hook类fixture需要测试用例testcase（_test_two）形式调用fixture
# @pytest.fixture()
# def _test_two():
#     print("===================testtwo==============")
#
# #不支持类形式fixtures
# # @pytest.fixture()
# # class conftest():
# #     @pytest.fixture()
# #     def _set_token(self):
# #         print("===================testone==============")
# #         token = _get_token()

#特殊hook类fixture不需要在测试用例处调用，系统会自动识别并调用
#所有函数前调用
def pytest_runtest_setup():
    print("===================setup==============")
    # token = _get_token()

#扩展命令行参数
# def pytest_addoption(parser):
#     parser.addoption("--ip_type", action="store", default="loopback",
#                      help="ip type includes loopback, domain and local_network")

#
def pytest_collection_modifyitems():
    print("===================pytest_collection_modifyitems==============")
