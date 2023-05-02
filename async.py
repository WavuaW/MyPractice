import asyncio

#coroutines - any funstion that has the async before it

async def main():
    print('Tim')
#async event-loop

#the coroutine becomes the entry point to the program
asyncio.run(main())