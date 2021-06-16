#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_ttt.py 
@Time   :   2021/6/15 21:34   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import pytest


class Testwg():
    # def __init__(self):
    #     pass
    @classmethod
    def setup_class(cls):
        pass
    @classmethod
    def _func1(self):
        print("test_wg")


class Testwgg(Testwg):
    # def __init__(self):
    #     super().__init__()
    #     print("init")
    @pytest.fixture(scope='class',autouse=True)
    def fixture_first(self):
        print("fixture1")

    @classmethod
    def setup_class(cls):
        super().setup_class()
        print("setup_class", cls.__class__)
        cls._func1()

    def _func2(self):
        print(self.__class__)
        self._func1()
        print("testwgg")


class Test_wggg(Testwgg):
    def test_func3(self):
        self._func2()

    def test_func4(self):
        print("test_func4")