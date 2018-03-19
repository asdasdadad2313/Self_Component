# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SSHConn
   Description :
   Author :       linhanqiu
   date：          3/19/18
-------------------------------------------------
   Change Activity:
                   3/19/18:
-------------------------------------------------
"""
__author__ = 'linhanqiu'

from Base import BaseConn
from Paramiko_Server_Manage.utils import resdec
import paramiko
import os


class SSHConn(metaclass=BaseConn):
    @classmethod
    def connect(cls, type, **kwargs):
        info = ''
        sets = ('hostname', 'username')
        for i in sets:
            if i not in kwargs:
                raise KeyError
        if type == 'up':
            try:
                cls.ssh.connect(
                    hostname=kwargs.get('hostname'),
                    port=kwargs.get('port', 22),
                    username=kwargs.get('username'),
                    password=kwargs.get('password')
                )
                info = '已连接'
            except paramiko.ssh_exception.AuthenticationException as e:
                cls.ssh.close()
                info = '连接失败-验证错误'
            except Exception as e:
                info = e
        elif type == 'kf':
            privatekey = os.path.expanduser(kwargs.get('path'))
            private_key = paramiko.RSAKey.from_private_key_file(privatekey)
            try:
                cls.ssh.connect(
                    hostname=kwargs.get('hostname'),
                    port=kwargs.get('port', 22),
                    username=kwargs.get('username'),
                    pkey=private_key
                )
            except paramiko.ssh_exception.AuthenticationException as e:
                cls.ssh.close()
                info = '连接失败-验证错误'
            except Exception as e:
                info = e
            info = '已连接'
        elif type == 'sf':
            cls.sf = cls.sfc((kwargs.get('hostname'), kwargs.get('port', 22)))
            privatekey = os.path.expanduser(kwargs.get('path'))
            private_key = paramiko.RSAKey.from_private_key_file(privatekey)
            try:
                cls.sf.connect(username='root', pkey=private_key)
            except paramiko.ssh_exception.AuthenticationException as e:
                cls.sf.close()
                info = '连接失败-验证错误'
            except Exception as e:
                info = e
            info = '已连接'
        else:
            info = '未选择连接方式'
        print(info)

    @classmethod
    def command(cls, com):
        command_info = ''
        try:
            if not com:
                command_info = '指令为空'
                result = ''
            else:
                stdin, stdout, stderr = cls.ssh.exec_command(com)
                result = resdec(stdout.read())
        except Exception as e:
            command_info = e
        if command_info:
            print(command_info)
        if result:
            print(result)

    @classmethod
    def sftp(cls, type, local, remote):
        sftp = paramiko.SFTPClient.from_transport(cls.sf)
        if type == 'get':
            sftp.get(remote, local)
        elif type == 'put':
            sftp.put(remote, local)
        else:
            pass

    @classmethod
    def __del__(cls):
        cls.ssh.close()
        cls.sfc.close()



