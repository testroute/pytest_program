# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# """
# @File   :   TestFile.py
# @Time   :   2021-06-09 0:25
# @Contact    :
# @Author     :   WG
# @Version    :   v 0.1
# @Desc  :
# """
# test_data = [{"test_input": "3+5",
#               "expected": 8,
#               "id": "验证3+5=8"
#               },
#              {"test_input": "2+4",
#               "expected": 6,
#               "id": "验证2+4=6"
#               },
#              {"test_input": "6 * 9",
#               "expected": 42,
#               "id": "验证6*9=42"
#               }
#              ]
#
#
# def pytest_generate_tests(metafunc):
#     ids = []
#     if "parameters" in metafunc.fixturenames:
#         for data in test_data:  # 用test_data中的id作为测试用例名称
#             ids.append(data['id'])
#         metafunc.parametrize("parameters", test_data, ids=ids, scope="function")  # 用test_data这个列表对parameters进行参数化。
#
#
# def test_eval(parameters):
#     assert eval(parameters['test_input']) == parameters['expected']

# import os
# import re
# import pytest
# import time
#
# def get_ping_response(ip_addr):
#     pid = os.popen("ping " + ip_addr)
#     prompt = pid.read()
#     m = re.search(r"Sent = (\d+), Received = (\d+), Lost = (\d+) \((\d+)% loss\)", prompt)
#     sent_num = int(m.group(1))
#     recv_num = int(m.group(2))
#     lost_num = int(m.group(3))
#     lost_rate = int(m.group(4))
#     return sent_num, recv_num, lost_num, lost_rate
#
#
# def test_case(request):
#     ip_type = request.config.getoption("ip_type")
#     if ip_type == "loopback":
#         assert get_ping_response("127.0.0.1")[3] == 0
#     elif ip_type == "local":
#         assert get_ping_response("192.168.1.1")[3] == 0
#     else:
#         raise Exception("failure")
import unittest

import pytest


@pytest.mark.usefixtures("set_driver")
class Tests:
    def test_func1(self):
        sd = self.login_class
        sd.login_by_token()
        print("===================test_func1==============")
        assert True

    def test_func2(self):
        print("===================test_func2==============")
        assert True