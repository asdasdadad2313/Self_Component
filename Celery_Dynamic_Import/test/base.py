# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base
   Description :
   Author :       linhanqiu
   date：          3/19/18
-------------------------------------------------
   Change Activity:
                   3/19/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from main.celery import execute
execute.delay('main.task.all_tasks.add1', 2, 444)
