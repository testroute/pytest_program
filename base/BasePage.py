#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   BasePage.py
@Time   :   2021-05-18 23:54   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
from selenium import webdriver

from common import MyLogger


class BasePage():
    def __init__(self,driver:webdriver=None):
        self.driver = driver
        self.log = MyLogger.logger

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(*locator).click()


    def find_and_get_text(self, locator):
        return self.find(locator).text
