#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_db.py 
@Time   :   2021-07-23 8:52   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
import datetime

from base.db import session
from base.models.test_case import TestCase


def test_add():
    tc1=TestCase(
    id = 10086,
    case_data ='测试用例内容',
    case_name = '用例名称',
    remark = '备注',
    del_flag = 1,
    create_user_id = 1,
    create_time = datetime.datetime.now(),
    update_time=datetime.datetime.now()
    )
    session.add(tc1)
    session.commit()  # 提交到数据库
