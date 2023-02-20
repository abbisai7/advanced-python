#asyncio-no need of mutliprocessing

import asyncio

async def coroutine1():
    print("CR1 is running on event loop,yield control,I am blocked for 4 secs")
    await asyncio.sleep(4)
    print("CR1 IS RESUMED")

async def coroutine2():
    print("CR2 is running on event loop,yield control,I am blocked for 4 secs")
    await asyncio.sleep(4)
    print("CR2 IS RESUMED")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(coroutine1(),coroutine2()))
    print("I am doing something else")
    print("done")
    