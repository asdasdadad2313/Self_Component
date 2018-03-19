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
# 两种方式调用
# execute.delay('main.task.all_tasks.add', 2, 444)
# execute.apply_async(args=['main.task.all_tasks.add',100,50])

# 链式调用，先执行第一个任务，接着执行第二个任务，类似add(add(1,3),3)
from main.task.chain_task import add,xsum
from celery import chain
# add.apply_async((1,3),link = add.s(3))
# chain(add.s(1,2),add.s(3),add.s(4))()

# 组并发调用
from celery import group
# group(add.s(1, 2), add.s(3,4), add.s(5,6))()

# 组并发调用带回调
from celery import chord
chord((add.s(1, 2), add.s(3,4), add.s(5,6)),xsum.s())()