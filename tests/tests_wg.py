#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   tests_wg.py 
@Time   :   2021-05-26 23:13   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Testwg():
    # def __init__(self):
    #     print("init")
    # @classmethod
    # def setup_class(cls):
    #     pass
    def test_func1(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://47.110.37.80:8088/#/")
        # print(self.driver.window_handles)
        self.driver.find_elements_by_tag_name("input")[0].send_keys("wg123")
        self.driver.find_elements_by_tag_name("input")[1].send_keys("123")
        self.driver.find_elements_by_tag_name("button")[0].click()
        time.sleep(3)
        #//a[contains(text(),"百度搜索")]
        # WebDriverWait(10.,0.5).until(EC.element_to_be_clickable((By.XPATH,'//*[@role="tab")]')))
        # self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get('http://47.110.37.80:8088/#/home/jenkins')
        self.driver.find_element_by_xpath("//div[contains(text(),'任务管理')]").click()
        # ele = self.driver.find_elements_by_xpath('//*[@role="tab"]')
        # print(ele)
        time.sleep(10)
