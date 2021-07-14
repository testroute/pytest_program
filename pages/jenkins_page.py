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
from pages.task_page import TaskPage


class JenkinsPage(MyBaseCase):
    def goto_task(self):
        self.run_steps("../datas/page_data/jenkins.yaml", 'goto_task')
        return TaskPage(self)
