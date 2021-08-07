#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_testcasepage.py
@Time   :   2021/7/13 19:25   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import pytest
from parameterized import parameterized

from base.base_case import MyBaseCase
from common.CommonFuncs import get_test_datas


class TestTestcasePage(MyBaseCase):
    @parameterized.expand(get_test_datas("TestTestcasePage.yaml","test_add_test"))#参数为双层中括号形式[[3, 3, 6],[1000, 1000, 2000]]
    def test_add_test(self,casename,title,desc):
        self.main.goto_test().add_testcase().input_casename(title).input_casetext(desc).confirm()
        self.assert_element_visible(f"//td[text()='{title}']")


    def test_goto_main(self):
        self.main.goto_test().goto_task()
        assert True

