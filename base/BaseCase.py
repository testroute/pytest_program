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

from common.CommonFuncs import _confirmLogin, _read_param, _update_token_and_return, _read_url


class basecase(BaseCase):
    log = MyLogger.logger
    _env = None
    __token = None
    _url = None

    # 针对测试类的每个用例前都会执行，不使用与方法
    def setUp(self, *args):
        super(basecase, self).setUp(*args)
        if self._env:
            pass
        else:
            self._env = 'test'
        self._url = _read_url(self._env)
        self.open(self._url)
        js = 'window.localStorage.getItem("token")'
        self.__token = self.execute_script(script=js)

        if _confirmLogin(self.__token):
            js = 'window.localStorage.setItem("token","%s")' % self.__token
            self.execute_script(script=js)
        else:
            __token = _update_token_and_return()
            js = 'window.localStorage.setItem("token","%s")' % self.__token
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
