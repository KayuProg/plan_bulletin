import asyncio

async def task1(name):
    print(f"{name}")
    
    await asyncio.sleep(1)
    
    print("helllo")
    
    return name

async def task2(name):
    print(f"{name},to ")
    
    await asyncio.sleep(2)
    
    print("good night")
    
    return name

async def main():
    result =await asyncio.gather(
        task1("a"),
        task2("b"),
    )
    print(result)
    
    
asyncio.run(main())