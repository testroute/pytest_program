#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_syscount.py 
@Time   :   2021-07-17 18:28   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""


class A(object):
    def __init__(self):
        self.child = None

    def destroy(self):
        self.child = None


class B(object):
    def __init__(self):
        self.parent = None

    def destroy(self):
        self.parent = None


def test3():
    a = A()
    b = B()
    a.child = b
    b.parent = a
