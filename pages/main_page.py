#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   main_page.py 
@Time   :   2021/7/13 19:26   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""

import unittest

import pytest

from base.base_case import MyBaseCase
from pages.jenkins_page import JenkinsPage


class MainPage(MyBaseCase):
    def goto_main(self):
        self.run_steps("../datas/page_data/main.yaml", 'goto_main')
        self.__called_setup = True
        return JenkinsPage(self)
# class MainPage(BasePage):
#     def gotoContact(self):
#         self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
#         sleep(1)
#         return ContactPage(self.driver)