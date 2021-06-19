#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_not_use_base.py 
@Time   :   2021/6/19 16:22   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import time

from selenium import webdriver


def test_func1():
    driver = webdriver.Chrome()
    driver.get("http://47.110.37.80:8088/#/")
    js = 'window.localStorage.setItem("token","%s")' % "a343aa1d900416d2c87731ece1db3843"
    driver.execute_script(js)
    time.sleep(3)
    driver.get("http://47.110.37.80:8088/#/home/jenkins")
    time.sleep(3)
    print("ok")
