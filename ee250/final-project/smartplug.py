import asyncio
from kasa import SmartPlug

async def main():
    p = SmartPlug("192.168.1.169")
    await p.turn_off()
    await p.update()
    print(p.alias)
    #t = await p.get_time()
    print(await p.get_time())
    


if __name__ == "__main__":
    asyncio.run(main())