# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_servers
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
import sqlalchemy as sa
import aiomysql
from aiomysql.sa import create_engine, SAConnection


class Table:
    metadata = sa.MetaData()

    tbl = sa.Table('t_area', metadata,
                   sa.Column('id', sa.Integer, primary_key=True),
                   sa.Column('code', sa.String(255)))

    @classmethod
    def servers(cls):
        return cls.tbl


async def GetServers(loop):
    datas = []
    engine = await create_engine(user='es',
                                 db='cityparlor',
                                 host='117.78.60.108',
                                 password='123456')
    async with aiomysql.create_pool(user='es',
                                    db='cityparlor',
                                    host='117.78.60.108',
                                    password='123456',
                                    loop=loop) as pool:
        async with pool.acquire() as conn:
            pool = SAConnection(connection=conn, engine=engine)
            async for row in pool.execute(Table.servers().select().limit(1)):
                datas.append((row.id,row.code))
    engine.close()
    await engine.wait_closed()
    return datas

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(GetServers(loop))
