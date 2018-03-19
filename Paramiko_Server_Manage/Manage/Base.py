# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Base
   Description :
   Author :       linhanqiu
   date：          3/19/18
-------------------------------------------------
   Change Activity:
                   3/19/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'
import asyncio


class BaseManage(type):
    def __new__(cls, name, bases, attrs):
        try:
            import uvloop
        except ImportError as e:
            pass
        attrs['loop'] = asyncio.get_event_loop()
        return type.__new__(cls, name, bases, attrs)
