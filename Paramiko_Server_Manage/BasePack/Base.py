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

import paramiko
from functools import partial


class BaseConn(type):
    def __new__(cls, name, bases, attrs):
        attrs['ssh'] = paramiko.SSHClient()
        attrs['ssh'].set_missing_host_key_policy(paramiko.AutoAddPolicy())
        attrs['sfc'] = partial(paramiko.Transport)
        return type.__new__(cls, name, bases, attrs)
