# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     chain_task
   Description :
   Author :       linhanqiu
   date：          3/19/18
-------------------------------------------------
   Change Activity:
                   3/19/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from main.celery import Runner

@Runner.task
def add(x=3, y=8):
    return x + y

@Runner.task
def xsum(values):
    return sum(values)