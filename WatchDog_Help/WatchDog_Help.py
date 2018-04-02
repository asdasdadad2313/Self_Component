# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WatchDog_Help
   Description :
   Author :       linhanqiu
   date：          4/2/18
-------------------------------------------------
   Change Activity:
                   4/2/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

# -*-coding:utf-8-*-
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
from pathlib import Path


class FileEventHandler_data(FileSystemEventHandler):
    # 数据文件夹监控
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        # 文件创建事件
        if event.is_directory:
            pass
        else:
            name = Path(event.src_path).name
            print(name)
            shutil.move(
                event.src_path,
                '/home/admin/spider2flume/data/' + name)


class FileEventHandler_log(FileSystemEventHandler):
    # 日志文件夹监控
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        # 文件创建事件
        if event.is_directory:
            pass
        else:
            name = Path(event.src_path).name
            print(name)
            shutil.move(
                event.src_path,
                '/home/admin/spider2flume/log/' + name)


def Monitor_Init(handle, path):
    # 监控子项实例化
    if path:
        observer = Observer()
        observer.schedule(handle, path, True)
    return observer


if __name__ == "__main__":
    # 实例化事件处理
    event_handler_data,event_handler_log = FileEventHandler_data(),FileEventHandler_log()

    # 获取待监控文件夹
    paths_data = [str(Path(i / 'KTspider/data/')) for i in Path(
        '/home/Code/LINHANQIU').iterdir() if Path(i).is_dir() and not str(i).endswith("Utils")]
    paths_log = [str(Path(i / 'KTspider/log/')) for i in Path('/home/Code/LINHANQIU').iterdir()
                 if Path(i).is_dir() and not str(i).endswith("Utils")]

    # 监控实例
    Monitor_data_tasks = [
        Monitor_Init(
            event_handler_data,
            i) for i in paths_data]
    Monitor_log_tasks = [Monitor_Init(event_handler_log, i) for i in paths_log]

    for i in Monitor_data_tasks:
        i.start()
    for i in Monitor_log_tasks:
        i.start()
    for i in Monitor_data_tasks:
        i.join()
    for i in Monitor_log_tasks:
        i.join()
