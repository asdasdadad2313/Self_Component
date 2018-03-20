# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     master
   Description :
   Author :       linhanqiu
   date：          3/20/18
-------------------------------------------------
   Change Activity:
                   3/20/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from nameko.rpc import rpc

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)