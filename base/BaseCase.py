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
import yaml

from common import MyLogger
from seleniumbase.fixtures.base_case import BaseCase

from common.CommonFuncs import _getToken, _confirmLogin


class basecase(BaseCase):
    log = MyLogger.logger
    __token = '3e167c28e2f2b962bf6e9c80543470e6'

    # 每个用例前都会执行
    def __init__(self, *args, **kwargs):
        # self.browser = 'Edge'
        # self.settings_file = None
        # self.device_metrics = None
        # self.mobile_emulator = None
        # self.dashboard = None
        # self._reuse_session = None
        # self.headless = None
        # self.locale_code = None
        # self.protocol = None
        # self.servername = None
        # self.port = None
        # self.proxy_string = None
        # self.user_agent = None
        # self.cap_file = None
        # self.cap_string = None
        super(basecase, self).__init__(*args, **kwargs)

    # 每个用例前都会执行
    # def setUp(self, *args):
    #     super(basecase, self).setUp(*args)

    # class前执行一次
    def setup_class(self, *args):
        if _confirmLogin(self.__token):
            js = 'window.localStorage.setItem("token",%s)' % self.__token
            self.driver.excute_scripts(js)
        else:
            __token = _getToken()
            js = 'window.localStorage.setItem("token",%s)' % self.__token
            self.driver.excute_scripts(js)

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
