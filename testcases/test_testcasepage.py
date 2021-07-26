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
from base.base_case import MyBaseCase


class TestTestcasePage(MyBaseCase):
    def test_add_test(self):
        self.main.goto_test().add_testcase().input_casename("test1").input_casetext("test1文本描述").confirm()
        self.assert_element_visible("//td[text()='test1']")


    def test_goto_main(self):
        self.main.goto_test().goto_task()
        assert True

