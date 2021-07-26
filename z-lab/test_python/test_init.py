#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_init.py 
@Time   :   2021/7/15 10:21   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""


class A:
    def __init__(self):
        self.a = "hello"

    def funca(self):
        pass


class B(A):
    def __init__(self):
        super(B, self).__init__()
    def funcb(self):
        pass


def test_init():
    clsb = B()
    clsa = A()
    print(hasattr(clsb, "a"))
    print(hasattr(A, "a"))
    print(hasattr(clsa, "a"))
    print(hasattr(clsb, "funcb"))
