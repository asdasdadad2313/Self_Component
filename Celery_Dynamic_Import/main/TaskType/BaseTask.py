# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BaseTask
   Description :
   Author :       linhanqiu
   date：          3/19/18
-------------------------------------------------
   Change Activity:
                   3/19/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'
from celery import Task


class BaseTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('任务成功完成: {0}'.format(retval))
        return super(BaseTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('任务处理失败, 原因: {0}'.format(exc))
        return super(
            BaseTask,
            self).on_failure(
            exc,
            task_id,
            args,
            kwargs,
            einfo)
