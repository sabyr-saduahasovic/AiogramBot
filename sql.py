import asyncio
import asyncpg
import logging

from config import host, PG_PASS, PG_USER

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_db():
    create_db_command = open("create_db.sql", "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(user=PG_USER, password=PG_PASS, host=host, database='postgres')
    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table users created")


async def create_pool():
    return await asyncpg.create_pool(user=PG_USER,
                                     password=PG_PASS,
                                     host=host,
                                     database='postgres')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(create_db())
