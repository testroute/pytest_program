#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_case.py 
@Time   :   2021-07-22 8:46   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
from sqlalchemy import Column, Integer, String, ForeignKey,DATETIME
from base.db import Base


class TestCase(Base):
    """
    测试用例orm模型
    """
    __tablename__ = 'hogwarts_test_case'
    id = Column(Integer, primary_key=True, autoincrement=True)
    case_data = Column(String(30), nullable=False, comment='测试用例内容')
    case_name = Column(String(30), nullable=False, comment='用例名称')
    remark = Column(String(20), nullable=False, comment='备注')
    del_flag = Column(String(20), comment='删除标志 1 未删除 0 已删除')
    create_user_id = Column(String(20), nullable=True,comment='创建人id')
    create_time = Column(DATETIME,nullable=True, comment='创建时间')
    update_time = Column(DATETIME, nullable=True,comment='更新时间')


