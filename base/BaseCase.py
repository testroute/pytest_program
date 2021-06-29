#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   BaseCase.py 
@Time   :   2021-05-27 0:05   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import time

import pytest
import yaml

from common import MyLogger
from seleniumbase.fixtures.base_case import BaseCase

from common.CommonFuncs import _confirmLogin, _read_param, _update_token_and_return


class basecase(BaseCase):
    log = MyLogger.logger
    __token = _read_param('token')

    # def setUp(self):
    #     super(basecase, self).setUp()
    #     # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>
    #
    # def tearDown(self):
    #     self.save_teardown_screenshot()
    #     if self.has_exception():
    #         # <<< Run custom code if the test failed. >>>
    #         pass
    #     else:
    #         # <<< Run custom code if the test passed. >>>
    #         pass
    #     # (Wrap unreliable tearDown() code in a try/except block.)
    #     # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
    #     super(basecase, self).tearDown()

    # class前执行一次

    def run_steps(self, path, operation):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data[operation]
        for step in steps:
            if step['action'] == "find_and_click":
                self.find_and_click(step['locator'])

            elif step['action'] == "send":
                # print(step['locator'], step['key'])
                self.send(step['locator'], step['key'])

            elif step['action'] == "scroll_find_click":
                self.scroll_find_click(step['locator'])

            elif step['action'] == "find_and_get_text":
                self.find_and_get_text(step['locator'])
