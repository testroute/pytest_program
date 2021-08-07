#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   models.py.py 
@Time   :   2021-07-22 23:20   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""

#1.导入模块
import datetime
#引擎
from sqlalchemy import create_engine#基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# 字段类型
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

#2.创建基类
Base = declarative_base()

#3.定义表格
class Users(Base):
    __tablename__ = 'users'  # 数据库表名称
    id = Column(Integer, primary_key=True)  # id 主键
    name = Column(String(32), index=True, nullable=False)  # name列，索引，不可为空


    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'), #联合唯一
        # Index('ix_id_name', 'name', 'email'), #索引
    )

# 4.创建表
def init_db():
    # 创建引擎建立数据库连接
    engine = create_engine(
        #DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
        "mysql+pymysql://root:123@127.0.0.1:3306/tset?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    #会将当前执行文件中所有继承自Base类的类, 生成表
    Base.metadata.create_all(engine)


#4.删除表格
def drop_db():
    # 创建引擎建立数据库连接
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/tset?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    # 会将当前执行文件中所有继承自Base类的类, 删除表
    Base.metadata.drop_all(engine)

# 执行
if __name__ == '__main__':
    #删除表格
    drop_db()
    #创建表格
    # init_db()