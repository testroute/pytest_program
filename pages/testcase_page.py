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
import time
import unittest

import pytest

from base.base_page import BasePage


class TestcasePage(BasePage):
    def goto_task(self):
        self.cls.run_steps(self.testcase_path, 'goto_task')
        from pages.task_page import TaskPage
        return TaskPage(self.cls)

    def goto_main(self):
        self.cls.run_steps(self.testcase_path, 'goto_main')
        from pages.main_page import MainPage
        return MainPage(self.cls)

    def add_testcase(self):
        self.cls.run_steps(self.testcase_path, 'add_testcase')
        return self

    def input_casename(self,casename):
        self.cls.run_steps(self.testcase_path, 'input_casename', key=casename)
        return self

    def input_casetext(self,casetext):
        self.cls.run_steps(self.testcase_path, 'input_casetext', key=casetext)
        return self

    def confirm(self):
        self.cls.run_steps(self.testcase_path, 'confirm')
        return self
