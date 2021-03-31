from sql import create_pool
import asyncio
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError


class DatabaseManager:
    cur: Connection = asyncio.get_event_loop().run_until_complete(create_pool())
        
    async def query(self, arg, values=None):
        try:
            if values == None:
                await self.cur.execute(arg)
            else:
                await self.cur.execute(arg, *values)
        except UniqueViolationError:
            pass

    async def fetchone(self, arg, values=None):
        try:
            if values == None:
                row = await self.cur.fetchrow(arg)
            else:
                row = await self.cur.fetchrow(arg, *values)
            return row
        except UniqueViolationError:
            pass

    async def fetchall(self, arg, values=None):
        try:
            if values == None:
                row = await self.cur.fetch(arg)
            else:
                row = await self.cur.fetch(arg, *values)
            return row
        except UniqueViolationError:
            pass


'''

products: idx text, title text, body text, photo blob, price int, tag text

orders: cid int, usr_name text, usr_address text, products text

cart: cid int, idx text, quantity int ==> product_idx

categories: idx text, title text

wallet: cid int, balance real

questions: cid int, question text

'''
