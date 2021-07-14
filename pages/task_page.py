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
from base.base_page import BasePage


class TaskPage(BasePage):
    def goto_main(self):
        self.cls.run_steps("../datas/page_data/main.yaml", 'goto_task')
        from pages.main_page import MainPage
        return MainPage(self.cls)
