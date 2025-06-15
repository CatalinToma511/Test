import asyncio
import time

async def task1():
    while True:
        time.sleep(4)
        print("t1")

async def task2():
    while True:
        time.sleep(2)
        print("t2")

async def main_task():
    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2())
    ]
    await asyncio.gather(*tasks)

def run():
    asyncio.run(main_task())