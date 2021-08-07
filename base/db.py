#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   db.py 
@Time   :   2021-07-23 8:08   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :连接数据库，返回session
"""
from urllib import parse

from sqlalchemy import create_engine#基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
# 字段类型
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

#2.创建基类
from config.settings_file import DB_HOST,DB_PORT,DB_NAME,DB_PASSWORD,DB_USERNAME

Base = declarative_base()
#特殊字符处理
passowrd = parse.quote_plus(DB_PASSWORD)

engine = create_engine(
    #DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    url=f"mysql+pymysql://{DB_USERNAME}:{passowrd}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
# 3.
Session = sessionmaker(bind=engine)
# 每次执行数据库操作时，都需要创建一个Connection
session = Session()