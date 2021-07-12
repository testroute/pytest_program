#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   testmytest.py 
@Time   :   2021-06-09 23:12   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import time

import pytest

from base.BaseCase import basecase

#在setup里open，然后reuse
# @pytest.mark.usefixtures("set_driver")
class TestClass(basecase):

    def test_basics(self):
        # self.login_class.login_by_token(self)
        #任务管理
        url = "http://47.110.37.80:8088/#/home/jenkins"
        self.open(url)
        self.click(selector='//div[contains(text(),"任务管理")]')
        time.sleep(1)
        # print("testcase:",time.time())
        # assert 1==1


    def test_two(self):
        assert 1==1

def test_request_sb_fixture(request):
    # sb = request.getfixturevalue("sb")
    # lc = request.getfixturevalue("set_driver")
    # url = "http://47.110.37.80:8088/#/home/jenkins"
    # sb.open(url)
    # lc.login_by_token(sb)
    # sb.open(url)
    # time.sleep(5)
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()