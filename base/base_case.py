#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   base_case.py
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

from common.CommonFuncs import _confirmLogin, _update_token_and_return, _read_url


class MyBaseCase(BaseCase):
    log = MyLogger.logger
    _env = None
    _url = None
    __token = None
    __need_login = True

    # def __init__(self, *args, **kwargs):
    #     super(BaseCase, self).__init__(*args, **kwargs)
    #     print("MyBaseCase",self.__class__)

    def setUp(self, *args):
        """
        针对测试类中的每个用例执行登录（已登录时不执行）；function testcase不执行。
        对于function testcase实现登录可用fixture，参考testcases/test_my_test.py
        中的test_request_sb_fixture
        """
        # <<< Run custom setUp() code for z-lab AFTER the super().setUp() >>>
        super(MyBaseCase, self).setUp(*args)
        if self._env:
            self.log.info("当前环境为：%s" % self._env)
        else:
            self._env = 'test'
            self.log.info("当前环境为：%s" % self._env)

        self._url = _read_url(self._env)
        self.log.info("初始化url为：%s" % self._url)
        if self.__need_login:
            self._login()
        from pages.main_page import MainPage
        self.main = MainPage(self)

    def _login(self):
        self.open(self._url)
        self.__token = _update_token_and_return()
        js = 'window.localStorage.setItem("token","%s")' % self.__token
        self.execute_script(script=js)
        if self._reuse_session:
            self.__need_login = False

    def run_steps(self, path, operation):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data[operation]
        for step in steps:
            if step['action'] == "open":
                self.open(step['url'])

            elif step['action'] == "click":
                self.click(step['locator'])

            elif step['action'] == "sendkey":
                self.send_keys(step['locator'], step['key'])

            elif step['action'] == "clicktext":
                self.click_link_text(step['text'])
    # def tearDown(self):
    # self.save_teardown_screenshot()
    # if self.has_exception():
    #     # <<< Run custom code if the test failed. >>>
    #     pass
    # else:
    #     # <<< Run custom code if the test passed. >>>
    #     pass
    # (Wrap unreliable tearDown() code in a try/except block.)
    # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
    # super(basecase, self).tearDown()

