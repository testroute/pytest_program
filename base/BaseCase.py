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
import os
import time

import pytest
import yaml

from common import MyLogger
from seleniumbase.fixtures.base_case import BaseCase

from common.CommonFuncs import _confirmLogin, _read_param, _update_token_and_return


class basecase(BaseCase):
    log = MyLogger.logger
    __token = _read_param('token')

    # 针对测试类的每个用例前都会执行，不使用与方法
    def setUp(self, *args):
        super(basecase, self).setUp(*args)
        THIS_URL = os.getenv('TEMP_URL', 'http://47.110.37.80:8088/#/')
        self.open(THIS_URL)
        __token = _read_param('token')
        if _confirmLogin(__token):
            js = 'window.localStorage.setItem("token","%s")' % __token
            self.execute_script(script=js)
        else:
            __token = _update_token_and_return()
            js = 'window.localStorage.setItem("token","%s")' % __token
            self.execute_script(script=js)
        # print("setup++++++++++:",time.time())




        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>
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
