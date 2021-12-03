import asyncio
from kasa import SmartPlug

async def main():
    p = SmartPlug("192.168.1.169")

    await p.update()
    print(p.alias)

    await p.turn_off()


if __name__ == "__main__":
    asyncio.run(main())