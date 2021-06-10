#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_setupclass.py 
@Time   :   2021/6/10 14:40   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import pytest


# 模块中的方法
def setup_module():
    print("setup_module：整个test_module.py模块只执行一次")


def teardown_module():
    print("teardown_module：整个test_module.py模块只执行一次")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


# 测试模块中的用例1
def test_one():
    print("正在执行测试模块----test_one")


# 测试模块中的用例2
def test_two():
    print("正在执行测试模块----test_two")


# 测试类
class TestCase():
    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup_method(self):
        print("setup_method: 每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method: 每个用例结束后执行")

    def setup(self):
        print("setup：每个用例开始前都会执行")

    def teardown(self):
        print("teardown：每个用例结束后都会执行")

    def test_three(self):
        print("正在执行测试类----test_three")

    def test_four(self):
        print("正在执行测试类----test_four")


if __name__ == "__main__":
    pytest.main(["-s", "test_setupclass.py"])
