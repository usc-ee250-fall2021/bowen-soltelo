from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import asyncio
from kasa import SmartPlug
import requests
OWM_API_KEY = '692176ded3c5179295c7e03db3edfc00'  # OpenWeatherMap API Key
DEFAULT_ZIP = 90089
dht_sensor_port = 8 
setRGB(0,128,0)
p = SmartPlug("192.168.1.169")
PORT_potentionmeter = 2
def get_weather(zip_code):
    params = {
        'appid': OWM_API_KEY,
        # TODO: referencing the API documentation, add the missing parameters for zip code and units (Fahrenheit)
        'zip' : DEFAULT_ZIP,
        'units' : 'matric'
    }

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params)

    if response.status_code == 200: # Status: OK
        data = response.json()

        # TODO: Extract the temperature & humidity from data, and return as a tuple
        main = data.get('main')
        return  main['temp'], main['humidity']

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0, 0.0
def weather_init():
    zip_code = DEFAULT_ZIP
    temp, hum = get_weather(zip_code)
    
    output = '{:.1f}F, {:>.0f}% humidity'.format(temp, hum)
    print('weather for {}: {}'.format(zip_code, output))

    return temp

async def main():
    count = 600
    temp = 0
    hum =0
    outside_temp = 0
    while True:
        try:
            threshold = analogRead(PORT_potentionmeter)
        
            if(threshold <= 100):
                goal =  17
            elif (threshold <= 200):
                goal = 18
            elif(threshold <=300):
                goal = 19
            elif(threshold<=400):
                goal = 20
            elif(threshold <= 500):
                goal = 21
            elif(threshold <= 600):
                goal = 22
            elif(threshold <= 700):
                goal = 23
            elif(threshold <= 800):
                goal = 24
            elif(threshold <= 900):
                goal = 25
            else :
                goal = 26
            if (count == 600):
                count = 0
                [ temp,hum ] = dht(dht_sensor_port,0)
                print("temp =", temp, "C\thumidity =", hum,"%")

                if isnan(temp) is True or isnan(hum) is True:
                    raise TypeError('nan error')
                
                outside_temp = weather_init()

                await p.update()
                time = await p.get_time()
                if temp >= goal and p.is_on:
                    print(p.alias + " Is going to sleep at ")
                    print(time)
                    await p.turn_off()
                if temp < goal  and goal > (outside_temp)  and p.is_off :
                    print(p.alias + "Is waking up at ")
                    print(time)
                    await p.turn_on()
            count +=1
            if (temp == goal):
                setRGB(0,128,0)
            else:
                setRGB(128,0,0)
            t = str(temp)
            h = str(hum)
            g = str(goal)
                # instead of inserting a bunch of whitespace, we can just insert a \n
                # we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
            setText_norefresh("Temp:" + t + "C H:" + g + "C\n" + "Humidity :" + h + "%")

        except (IOError, TypeError) as e:
            print(str(e))
            setText("")

        except KeyboardInterrupt as e:
            print(str(e))
            setText("")
            break

        # wait some time before re-updating the LCD
        sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
