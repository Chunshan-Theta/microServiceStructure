import aredis
import os

# import asyncio
# import json


class Queue(object):
    HOST = os.environ.get("REDIS_HOST", default="127.0.0.1")
    PORT = os.environ.get("REDIS_PORT", default="6379")

    def __init__(self, name, namespace='queue', **redis_kwargs):
        # redis的默认参数为：host='localhost', port=6379, db=0， 其中db为定义redis database的数量
        redis_kwargs["host"] = self.HOST
        redis_kwargs["port"] = self.PORT
        self.__client = aredis.StrictRedis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    async def qsize(self):
        return await self.__client.llen(self.key)  # 返回队列里面list内元素的数量

    async def enqueue(self, item):
        await self.__client.rpush(self.key, item)  # 添加新元素到队列最右方

    # def get_wait(self, timeout=None):

    async def dequeue_nowait(self):
        # 直接返回队列第一个元素，如果队列为空返回的是None
        item = await self.__client.lpop(self.key)
        if item is None:
            return None
        message = item.decode("utf-8")
        # message = json.loads(message.decode("utf-8"))
        return message

    async def set_msg_by_direct_id_ex(self, id, second2expire, value):
        await self.__client.setex(id, second2expire, value)  # set message by direct id

    async def get_msg_by_direct_id(self, id):
        item = await self.__client.get(id) # get message by direct id
        if item:
            item = item.decode("utf-8")
        return item
