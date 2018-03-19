# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Management
   Description :
   Author :       linhanqiu
   date：          3/19/18
-------------------------------------------------
   Change Activity:
                   3/19/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from Base import BaseManage
#
import sys
import os
sys.path.append(os.getcwd())
from Paramiko_Server_Manage.utils.get_servers import GetServers
import fire


class Managemnet(metaclass=BaseManage):
    @classmethod
    async def get_servers(cls):
        data = await GetServers(cls.loop)
        return data

    @classmethod
    def start(cls):
        # data -> [(id1,ip1),(id2,ip2)]
        datas = cls.loop.run_until_complete(cls.get_servers())
        for (i, ip) in datas:
            print()


def start():
    Managemnet.start()


fire.Fire(start)
