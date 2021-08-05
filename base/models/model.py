#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   model.py 
@Time   :   2021-07-22 23:25   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""

#1.导入模块
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# 导入models.py文件中类

#2.建立连接
from base.models.models import Users

engine = create_engine(
    #DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    "mysql+pymysql://root:123@127.0.0.1:3306/tset?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
# 3.
Session = sessionmaker(bind=engine)
# 每次执行数据库操作时，都需要创建一个Connection
session = Session()

# 4.增删改查############# 执行ORM操作 #############
obj1 = Users(name="owen")
session.add(obj1)

# 5.提交事务
session.commit()

# 关闭session，其实是将连接放回连接池
session.close()