#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   CommonFuncs.py
@Time   :   2021/6/7 20:13
@Contact    :
@Author     :   WG
@Version    :   v 0.1
@Desc   : 日志配置文件控制台or错误日志记录
"""
import logging.config
import sys
import os
import time


logfile_dir = os.path.join(os.path.dirname( os.path.dirname(__file__)), 'logs')
if not os.path.exists(logfile_dir):
    os.makedirs(logfile_dir)

logging_current_time = time.strftime( "%Y-%m-%d", time.localtime( time.time() ) )

dictLogConfig = {
        "version":1,
        'disable_existing_loggers': False,
        "formatters":{
            "myFormatter":{
                "format":'%(asctime)s [%(module)s:%(funcName)s:%(lineno)d][%(levelname)s]- %(message)s',
                "datefmt":'%Y-%m-%d %H:%M:%S'
                },
            "fileFormatter":{
                "format":'%(asctime)s [%(module)s:%(funcName)s:%(lineno)d][%(levelname)s]- %(message)s',
                "datefmt":'%Y-%m-%d %H:%M:%S'
                },
            },
        "handlers":{
                    "consoleHandler":{
                        "class":"logging.StreamHandler",
                        "formatter":"myFormatter"
                        },
                    'selectdb_handler': { 
                        'level':'DEBUG',
                        'class':'logging.handlers.RotatingFileHandler',
                        'filename':os.path.join(logfile_dir,'main_%s.log'%(  logging_current_time ) ),
                        #若是添加如下两项配置，日志不能重写，每次都是追加
                        #'maxBytes': 1024*1024*5,
                        #'backupCount': 5,
                        'formatter':'myFormatter',
                        #w为每次重写，a是追加
                        'mode':'a',
                        "encoding":"utf-8"
                        },
                    'error_handler': {
                        'level':'DEBUG',
                        'class':'logging.handlers.RotatingFileHandler',
                        'filename':os.path.join(logfile_dir,'error_%s.log'%(  logging_current_time ) ),
                        #若是添加如下两项配置，日志不能重写，每次都是追加
                        #'maxBytes': 1024*1024*5,
                        #'backupCount': 5,
                        'formatter':'fileFormatter',
                        #w为每次重写，a是追加
                        'mode':'a',
                        }
                    },
        "loggers":{
            'selectdb.logger': { 
                'handlers': ['selectdb_handler','consoleHandler'],
                'level': 'DEBUG', 
                'propagate': True
                },
            'error.logger': {
                'handlers': ['error_handler','consoleHandler'],
                'level': 'DEBUG',
                'propagate': True
            }

        }
}
"""
Formatter instances are used to convert a LogRecord to text.

Formatters need to know how a LogRecord is constructed. They are
responsible for converting a LogRecord to (usually) a string which can
be interpreted by either a human or an external system. The base Formatter
allows a formatting string to be specified. If none is supplied, the
default value of "%s(message)" is used.

The Formatter can be initialized with a format string which makes use of
knowledge of the LogRecord attributes - e.g. the default value mentioned
above makes use of the fact that the user's message and arguments are pre-
formatted into a LogRecord's message attribute. Currently, the useful
attributes in a LogRecord are described by:

%(name)s            Name of the logger (logging channel)
%(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                    WARNING, ERROR, CRITICAL)
%(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                    "WARNING", "ERROR", "CRITICAL")
%(pathname)s        Full pathname of the source file where the logging
                    call was issued (if available)
%(filename)s        Filename portion of pathname
%(module)s          Module (name portion of filename)
%(lineno)d          Source line number where the logging call was issued
                    (if available)
%(funcName)s        Function name
%(created)f         Time when the LogRecord was created (time.time()
                    return value)
%(asctime)s         Textual time when the LogRecord was created
%(msecs)d           Millisecond portion of the creation time
%(relativeCreated)d Time in milliseconds when the LogRecord was created,
                    relative to the time the logging module was loaded
                    (typically at application startup time)
%(thread)d          Thread ID (if available)
%(threadName)s      Thread name (if available)
%(process)d         Process ID (if available)
%(message)s         The result of record.getMessage(), computed just as
                    the record is emitted
"""
###########################################################################
## 全局环境变量
###########################################################################
#日志模块的加载
logging.config.dictConfig(dictLogConfig)
logger = logging.getLogger("selectdb.logger")
logger_error = logging.getLogger("error.logger")
