import asyncio

#coroutines - any funstion that has the async before it

async def main():
    print('Tim')
    #creating a task, the real power of asynchronous programming 
    task = asyncio.create_task(foo('Text'))
    #awaits the two second wait time
    # await task
    await asyncio.sleep(0.5)
    print('Finished')
async def foo(text):
    print(text)
    #using await - required to run a coroutine
    await asyncio.sleep(10)

#this creates the coroutine and becomes the entry point to the program
asyncio.run(main())