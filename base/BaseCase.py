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
from common import MyLogger
from seleniumbase.fixtures.base_case import BaseCase


class BaseCase(BaseCase):
    log = MyLogger.logger
    
    def __init__(self,*args, **kwargs):
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

        super(BaseCase, self).__init__(*args, **kwargs)


    def setup(self,*args):
        super(BaseCase, self).setUp(*args)
        print(self.is_pytest)
        print(self.driver.__class__)


