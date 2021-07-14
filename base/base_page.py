#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   base_page.py 
@Time   :   2021/7/14 18:04   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""

from base.base_case import MyBaseCase


class BasePage:
    def __init__(self,cls : MyBaseCase):
        self.cls = cls
        self.cls.open(self.cls._url.__add__('home/jenkins'))





