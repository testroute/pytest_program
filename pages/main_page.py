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
from pages.task_page import TaskPage


class MainPage(BasePage):
    def goto_task(self):
        self.cls.run_steps("../datas/page_data/main.yaml", 'goto_task')
        time.sleep(3)
        return TaskPage(self.cls)