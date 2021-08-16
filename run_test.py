#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   run_test.py 
@Time   :   2021-08-16 23:50   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :
"""
# encoding: utf-8
# 代码来源：全栈测开训练营

"""
所有案例执行并生成allure测试报告的执行策略
"""

import os
import sys
import threading
import pytest


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


project_root = os.path.dirname(__file__)
report_dir = os.path.join(project_root, 'report')
# 存放测试结果的目录，会生成一推json文件
result_dir = os.path.join(report_dir, 'allure_result')
allure_report = os.path.join(report_dir, 'allure_report')

allure = "allure"

#  定义搜索条件，搜索所有以test开头的用例
test_item = 'testcases\\test_testcasepage.py'


def run_pytest():
    # --clean-alluredir
    # pytest.main(['-vv', '-s', '-m', 'webtest', f'--alluredir={result_dir}', '--clean-alluredir'])
    #- pytest -s testcases\test_testcasepage.py --alluredir allure_reports
    # 执行前清除allure_result数据，避免生成报告时，会把上次执行的数据带进去
    pytest.main(['-vv', '-s', f'{test_item}', f'--alluredir={result_dir}', '--clean-alluredir'])


def general_report():
    # 调用cmd方法 report.allure，根据windows或linux环境判断- allure generate allure_reports -o allure_results --clean
    # 然后执行生成报告的方法generate
    # --clean 覆盖路径，将上次的结果覆盖掉
    cmd = "{} generate {} -o {} --clean".format(allure, result_dir, allure_report)
    # 执行命令行命令，并通过read()方法将命令的结果返回
    print(os.popen(cmd).read())


if __name__ == '__main__':
    #创建两个线程，分别执行两个方法
    run = threading.Thread(target=run_pytest)
    gen = threading.Thread(target=general_report)
    run.start()
    # 先执行第一个线程，这个线程执行完才会执行下面的线程和主线程
    run.join()
    gen.start()
    gen.join()


