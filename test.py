import asyncio

async def give_vert():
    await asyncio
    print(1)
    return '|'

async def gorizont():
    print('-',end='')
    await asyncio.sleep(2)

async def vertical(sym):
    print(sym)
    await asyncio.sleep(1)

async def main():
    while True:
        await asyncio.gather(gorizont(),vertical(give_vert()))

if __name__=='__main__':
    asyncio.run(main())