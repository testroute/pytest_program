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
# #curl -X POST "http://stuq.ceshiren.com:8089/user/login" -H "accept: */*" -H "token: 1" -H "Content-Type: application/json" -d "{ \"password\": \"123\", \"userName\": \"wg123\"}"
#
#
# def _get_token():
#     url = "http://stuq.ceshiren.com:8089/user/login"
#     body = {
#         "password": "123",
#         "userName": "wg123"
#     }
#     headers = {
#         "accept": "*/*",
#         "Content-Type": "application/json",
#         "token": "1"
#     }
#     res = requests.post(url,json=body,headers = headers)
#     _token = res.json()["data"]["token"]
#     return _token
# @pytest.fixture()
# def _test_two():
#     print("===================testtwo==============")
#     token = _get_token()
#
# #不支持类型fixtures
# # @pytest.fixture()
# # class conftest():
# #     @pytest.fixture()
# #     def _set_token(self):
# #         print("===================testone==============")
# #         token = _get_token()
def pytest_runtest_setup():
    print("===================setup==============")
    # token = _get_token()
#
# _get_token()

# def pytest_addoption(parser):
#     parser.addoption("--ip_type", action="store", default="loopback",
#                      help="ip type includes loopback, domain and local_network")


def pytest_collection_modifyitems():
    print("===================pytest_collection_modifyitems==============")
