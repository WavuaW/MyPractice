import asyncio

async def fetch_data():
    #you can only use await inside of an async function/inside an actual co routine.
    print('Start fetching')
    await asyncio.sleep(2)
    print('Done fetching')
    return {'data' : 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    #when you create a task and a coroutine returns a value this is called a Future(similar to promise in javascript)
    #these tasks subclass the 'Future'
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    
    #if you want the value returned form a coroutine you must await that coroutine/task
    value = await task1
    print(value)
    await task2
#just a comment

asyncio.run(main())