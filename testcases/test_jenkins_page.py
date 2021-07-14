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


class TestJenkinsPage(MyBaseCase):
    def test_goto_task(self):
        self.main.goto_task()
        assert True
