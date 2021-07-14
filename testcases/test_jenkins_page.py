#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_jenkins_page.py 
@Time   :   2021/7/13 19:25   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
from base.base_case import MyBaseCase
from pages.main_page import MainPage


class TestJenkinsPage:

    def setup_class(self):
        # 实例化 MainPage类
        self.main = MainPage()

    def test_goto_task(self):
        assert True
