import unittest
import requests
import datetime as dt
from config import APIKEY

def timeformat(integertimestamp):
    time = dt.datetime.fromtimestamp(integertimestamp)
    timestampformat = "%m/%d/%Y, %H:%M:%S GMT+06"
    timestamp = time.strftime(timestampformat)
    return timestamp

def weather(city):
    api_call = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}'
    r = requests.get(api_call)
    #format weather data
    weather_data = r.json()
    #chance_of_rain = weather_data.get('rain').get('1h') * 100
    Ftemp = (weather_data.get('main').get('temp') - 273.15) * (9/5) + 32
    #format time 
    time = timeformat(weather_data.get('dt')) 
    result = f'''city: {weather_data.get('name')}
{weather_data.get('weather')[0].get('description')}
current temperature: {Ftemp}
time: {time}
'''
    return weather_data

class test_weather(unittest.TestCase):

    def test_weather(self):
        testing = weather('Austin')
        print(testing)

if __name__ == "__main__":
    unittest.main()