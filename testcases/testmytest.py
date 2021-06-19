#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   testmytest.py 
@Time   :   2021-06-09 23:12   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import time

import pytest
from seleniumbase import BaseCase

from base.BaseCase import basecase


class MyTestClass(basecase):

    def test_basics(self):
        # self.browser
        # url = "https://store.xkcd.com/collections/posters"
        # self.open(url)
        # self.type('input[name="q"]', "xkcd book")
        # self.click('input[value="Search"]')
        # self.assert_text("xkcd: volume 0", "h3")
        # self.open("https://xkcd.com/353/")
        # self.assert_title("xkcd: Python")
        # self.assert_element('img[alt="Python"]')
        # self.click('a[rel="license"]')
        # self.assert_text("free to copy and reuse")
        # self.go_back()
        # self.click_link("About")
        # self.assert_exact_text("xkcd.com", "h2")
        url = "http://47.110.37.80:8088/#/"
        self.open(url)
        self.set_driver()

        #任务管理
        self.click('div[text="任务管理"]')
        time.sleep(3)
        url = "http://47.110.37.80:8088/#/home/jenkins"
        self.open(url)
        time.sleep(10)

    def test_two(self):
        print("testtwo")
        url = "http://47.110.37.80:8088/#/home/jenkins"
        self.open(url)


if __name__ == '__main__':
    pytest.main()