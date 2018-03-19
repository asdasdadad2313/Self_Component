# -*- coding: utf-8 -*-
from __future__ import absolute_import
"""
-------------------------------------------------
   File Name：     celery.py
   Description :
   Author :       linhanqiu
   date：          3/16/18
-------------------------------------------------
   Change Activity:
                   3/16/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

# import
from celery import Celery
from configparser import ConfigParser
from importlib import import_module, reload
import os
# class


class CeleryRunner:
    def __init__(self):
        self.conf = ConfigParser()
        self.confpath = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))),
            'conf.ini')
        self.conf.read(self.confpath)
        self.broker = self.conf.get('baseconf', 'broker')
        self.backend = self.conf.get('baseconf', 'backend')

    def __call__(self, *args, **kwargs):
        app = Celery('main',
                     broker=self.broker,
                     backend=self.backend,
                     )
        app.conf.CELERY_IMPORTS = ['main.task', 'main.task.all_tasks']
        return app


def import_string(import_name):
    import_name = str(import_name).replace(':', '.')
    modules = import_name.split('.')
    mod = import_module(modules[0])
    for comp in modules[1:]:
        if not hasattr(mod, comp):
            reload(mod)
        mod = getattr(mod, comp)
    return mod


from inspect import getmembers, isfunction


def get_tasks(module='task'):
    return [{
        'name': 'task:{}'.format(f[1].__name__),
        'doc': f[1].__doc__,
    } for f in getmembers(import_module(module), isfunction)]


Runner = CeleryRunner()()

# 引入任务


@Runner.task
def execute(func, *args, **kwargs):
    func = import_string(func)
    return func(*args, **kwargs)


if __name__ == '__main__':
    Runner.start()
