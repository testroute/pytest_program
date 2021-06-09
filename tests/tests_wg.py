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
str1 = "wg" if False else "wg2"
print(str1)
str2 = [i+"2" for i in str1]
str1 = [i+"2" for i in str1]
a = 1
b = 2
a,b=b,a
a,b = 1,2
print(a) if a == b else print(b)
a = 1
if a==1 :
    print("aaa")
print(str2,str1)