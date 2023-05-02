import asyncio

#coroutines - any funstion that has the async before it

async def main():
    print('Tim')
    await foo('Text')
    print('Finished')
async def foo(text):
    print(text)
    #using await - required to run a coroutine
    await asyncio.sleep(2)

#this creates the coroutine and becomes the entry point to the program
asyncio.run(main())