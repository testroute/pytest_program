#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   TestClass.py
@Time   :   2021-05-26 23:13   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
from seleniumbase import BaseCase
from  common.MyLogger import logger as log

class TestClass(BaseCase):
    def test_basics(self):
        url = "https://store.xkcd.com/collections/posters"
        self.open(url)
        self.type('input[name="q"]', "xkcd book")
        self.click('input[value="Search"]')
        self.assert_text("xkcd: volume 0", "h3")
        self.open("https://xkcd.com/353/")
        self.assert_title("xkcd: Python")
        self.assert_element('img[alt="Python"]')
        self.click('a[rel="license"]')
        self.assert_text("free to copy and reuse")
        self.go_back()
        self.click_link("About")
        log.info("wg+++++")
        self.assert_exact_text("xkcd.com", "h2")