#weatherbot.py

import os
from discord.ext import commands
from dotenv import load_dotenv
import requests
import datetime as dt
from config import APIKEY

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '`')

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
    return result

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command('t')
async def temp(ctx):
    weather_result = weather('Austin')
    await ctx.send(weather_result)

bot.run(TOKEN)