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
import os
import sys
import time
import unittest

import pytest

from base.base_page import BasePage
from pages.task_page import TaskPage
from pages.testcase_page import TestcasePage


class MainPage(BasePage):
    def goto_task(self):
        self.cls.run_steps(self.main_path, 'goto_task')
        return TaskPage(self.cls)

    def goto_test(self):
        self.cls.run_steps(self.main_path, 'goto_test')
        return TestcasePage(self.cls)
