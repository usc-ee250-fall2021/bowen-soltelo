import asyncio
from kasa import SmartPlug
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
dht_sensor_port = 7
setRGB(0,128,0)
p = SmartPlug("192.168.1.169")
while True:
	try:
        # get the temperature and Humidity from the DHT sensor
		[ temp,hum ] = dht(dht_sensor_port,0)
		print("temp =", temp, "C\thumidity =", hum,"%")

		# check if we have nans
		# if so, then raise a type error exception
		if isnan(temp) is True or isnan(hum) is True:
		    raise TypeError('nan error')

	    t = str(temp)
		h = str(hum)

        # instead of inserting a bunch of whitespace, we can just insert a \n
        # we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
		setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")

	except (IOError, TypeError) as e:
		print(str(e))
		# and since we got a type error
		# then reset the LCD's text
		setText("")

	except KeyboardInterrupt as e:
		print(str(e))
		# since we're exiting the program
		# it's better to leave the LCD with a blank text
		setText("")
		break

	# wait some time before re-updating the LCD
	sleep(5)