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

    def setUp(self):
        super(basecase, self).setUp()
        # <<< 如果只验证 以下页面可以直接setup中登陆>>>
        self.open("http://47.110.37.80:8088/#/")
        js = 'window.localStorage.setItem("token","a343aa1d900416d2c87731ece1db3843")'
        self.execute_script(script=js)
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



