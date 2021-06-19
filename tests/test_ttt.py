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

from tests.tests_wg import Testwg


class Testwgg(Testwg):
    # def __init__(self):
    #     print("init")

    @pytest.fixture(scope='class',autouse=True)
    def fixture_first(self):
        self._func1()
        print("fixture1")
    #
    def setup(self):
        print("here setup used")
    # @classmethod
    # def setup_class(cls):
    #     super().setup_class()
    #     print("setup_class", cls.__class__)
    #     cls._func1()

    def _func2(self):
        # print(self.__class__)
        self._func1()
        print("testwgg")


class Test_wggg(Testwgg):

    def test_func3(self):
        self._func2()

    def test_func4(self):
        print("test_func4")