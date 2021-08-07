#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   base_page.py 
@Time   :   2021/7/14 18:04   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   : 提供page对象通用方法
"""
import os
import sys

from base.base_case import MyBaseCase


class BasePage:
    """

    """
    def __init__(self,cls : MyBaseCase):
        self.cls = cls
        # print('object born id:%s' % str(hex(id(self))))
        # print("in basepage：", sys.getrefcount(self.cls))
        self.main_path = os.path.dirname(__file__).strip("base").__add__("pages\\page_data\\main.yaml")
        self.task_path = os.path.dirname(__file__).strip("base").__add__("pages\\page_data\\task.yaml")
        self.testcase_path = os.path.dirname(__file__).strip("base").__add__("pages\\page_data\\testcase.yaml")
        self.jenkins_path = os.path.dirname(__file__).strip("base").__add__("pages\\page_data\\jenkins.yaml")

    def destroy(self):
        """
        循坏调用时手动解循环
        :return: None
        """
        self.cls = None
