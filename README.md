# pytest_program

本项目实现web自动化的技术选型：Python+SeleniumBase+Pytest+YAML+Allure ，主要是针对本人搭建的个人项目来开展的，项目实现了自动配置浏览器driver，PO模型改造，数据驱动，数据清洗，重写setUp方法/利用pytest fixture机制实现登陆，环境配置，日志并拆分日志，错误截图以及allure报告展示等功能。

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

- allure_reports ====>> allure 数据采集目录
- allure_results ====>> html报告存放路径
- base ====>> 基本类，包括继承于seleniumBase.basecase的和BasePage对象
- common ====>> 通用方法存放地址
- config ====>> 配置文件
- datas ====>> 测试数据文件管理
- logs ====>> 日志文件存放地址
- pages ====>> Page对象
- requirements.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例
- z-lab.myfrane ====>>

## 测试执行
进入项目执行pytest testcase
或在[testcase](https://github.com/testroute/pytest_program/tree/main/testcases)下执行pytest test_my_test.py


## 测试报告效果展示

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务：

```
# 需要提前配置allure环境，才可以直接使用命令行
allure serve ./report
```

最终，可以看到测试报告的效果图如下：

![image.png](https://upload-images.jianshu.io/upload_images/16853007-248f805c82dbf99c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
