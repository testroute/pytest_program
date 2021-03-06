# pytest_program

本项目实现web自动化的技术选型：Python+SeleniumBase+Pytest+YAML+Allure ，主要是针对本人搭建的个人项目来开展的，项目实现了基于[conftest.set_driver](https://github.com/testroute/pytest_program/blob/main/testcases/conftest.py) or [setup](https://github.com/testroute/pytest_program/blob/main/base/base_case.py)填充cookie/token的自动登陆，[PO模型改造](https://github.com/testroute/pytest_program/tree/main/pages)，基于parameterized.expend的[数据驱动](https://github.com/testroute/pytest_program/blob/main/testcases/test_testcasepage.py)，使用pytest_runtest_setup hook函数针对测试item的[数据清洗](https://github.com/testroute/pytest_program/blob/main/testcases/conftest.py)，基于allure的测试报告生成以及环境配置、拆分日志等功能。

## 项目说明

本项目在实现过程中，把整个项目严格按照PO模型进行页面对象拆分，同时还包括数据配置、关键字封装、测试用例等模块。

目前已经实现了页面数据的数据驱动，为下一步进行Jenkins持续集成做准备。

## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```
无需安装浏览器driver即可实现系统默认浏览器的驱动，目前可使用Chrome，Firfox,Edge,Safari等主流浏览器，多个浏览器时，默认使用Chrome，可以使用 --browser指定浏览器。

```
pytest
```

## 项目结构

- reports ====>> allure 报告目录
- base ====>> 基本类，包括继承于seleniumBase.basecase的和BasePage对象
- common ====>> 通用方法存放地址
- config ====>> 配置文件
- datas ====>> 测试数据文件管理
- logs ====>> 日志文件存放地址
- pages ====>> Page对象
- requirements.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例
- z-lab.myfrane ====>>仅依赖selenium/appnium搭建的web/app自动化框架

## 测试执行
进入项目执行pytest testcase
或在[根目录](https://github.com/testroute/pytest_program)下执行pytest test_my_test.py


## 测试报告效果展示
- 根目录下执行python run_test.py


```
# 需要提前配置allure环境，才可以直接使用命令行
```

最终，可以看到测试报告的效果图如下：
![image](https://user-images.githubusercontent.com/55448903/128596967-c92497c9-e5b2-4994-a63d-15d2dd55524c.png)
