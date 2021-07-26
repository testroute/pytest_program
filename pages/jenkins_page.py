#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   jenkins_page.py
@Time   :   2021-05-26 23:43   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import unittest

import pytest

from base.base_case import BaseCase, MyBaseCase
from base.base_page import BasePage
from pages.task_page import TaskPage


class JenkinsPage(BasePage):
    def goto_task(self):
        self.cls.run_steps(self.task_path, 'goto_task')
        return TaskPage(self.cls)
