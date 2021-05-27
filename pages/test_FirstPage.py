#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_FirstPage.py
@Time   :   2021-05-26 23:43   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import unittest

import pytest

from base.BaseCase import BaseCase
from base.BasePage import BasePage
class Test_FirstPage(BaseCase):
    def test_log(self):
        print(1)
        self.log.info("wg")
        assert True
    def test_pt(self):
        assert 1==2

if __name__ == '__main__':
    pytest.main(['-s', 'test_FirstPage.py'])