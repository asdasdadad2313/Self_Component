# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     reply
   Description :
   Author :       linhanqiu
   date：          3/22/18
-------------------------------------------------
   Change Activity:
                   3/22/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'


class Reply:
    def __init__(self):
        self.reply = "基本回复-"


class StrangerReply(Reply):
    def __init__(self):
        super(StrangerReply, self).__init__()
        self.custom = "陌生人"
        self.reply += self.custom


class FriendReply(Reply):
    def __init__(self):
        super(FriendReply, self).__init__()
        self.custom = "朋友"
        self.reply += self.custom


if __name__ == '__main__':
    test = StrangerReply()
