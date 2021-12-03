from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import asyncio
from kasa import SmartPlug
dht_sensor_port = 7 
setRGB(0,128,0)
p = SmartPlug("192.168.1.169")
#async def main(temp):
 #   await p.update()
 #   if temp == 23 and p.is_on:
  #      print(p.alias + "Is going to sleep")
  #      await p.turn_off()
  #  if temp < 23 and p.is_off:
   #     print(p.alias + "Is waking up")
   #     await p.turn_on()
#async def on():
#    await p.update()
 #   if p.is_off:
 #       print(p.alias + "Is waking up")
 #       await p.turn_on()
#async def off():
 #   await p.update()
 #   if p.is_on:
 #       print(p.alias + "Is going to sleep")
  #      await p.turn_off()
async def main():
    while True:
        try:
            [ temp,hum ] = dht(dht_sensor_port,0)
            print("temp =", temp, "C\thumidity =", hum,"%")

            if isnan(temp) is True or isnan(hum) is True:
                raise TypeError('nan error')

            await p.update()
            if temp == 23 and p.is_on:
                print(p.alias + "Is going to sleep")
                await p.turn_off()
            if temp < 23 and p.is_off:
                print(p.alias + "Is waking up")
                await p.turn_on()
            #asyncio.run(main(temp))
            #if temp < 23:
            #   asyncio.run(on())
            #if temp == 23:
            #   asyncio.run(off())
            t = str(temp)
            h = str(hum)

            # instead of inserting a bunch of whitespace, we can just insert a \n
            # we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
            setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")

        except (IOError, TypeError) as e:
            print(str(e))
            setText("")

        except KeyboardInterrupt as e:
            print(str(e))
            setText("")
            break

        # wait some time before re-updating the LCD
        sleep(5)

if __name__ == "__main__":
    asyncio.run(main())