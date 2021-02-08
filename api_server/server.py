from util.aredis_queue import Queue
import asyncio

redis_to_MDL = Queue(name="MDL", namespace="common")
redis_to_API = Queue(name="API", namespace="common")


async def new_work(item):
    print(f"new_work: {item}")
    await redis_to_MDL.enqueue(item)


async def get_responds():
    res = await redis_to_API.dequeue_nowait()
    print(f"get_responds: {res}")
    return res


async def main():
    tasks = [
        "world 1",
        "world 2",
        "world 3",
    ]
    #
    tasks_sum = len(tasks)
    tasks_idx = 0
    #
    for t in tasks:
        await new_work(t)

    while tasks_sum > tasks_idx:
        print(await get_responds())
        await asyncio.sleep(1)


asyncio.run(main())