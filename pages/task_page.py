#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   main_page.py 
@Time   :   2021/7/13 19:26   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""

import unittest

import pytest

from base.base_case import MyBaseCase


class TaskPage(MyBaseCase):
    def goto_main(self):
        self.run_steps("../datas/page_data/main.yaml", 'goto_task')
        from pages.jenkins_page import JenkinsPage
        return JenkinsPage()
