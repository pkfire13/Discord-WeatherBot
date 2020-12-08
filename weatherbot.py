#weatherbot.py

import os
from discord.ext import commands
from dotenv import load_dotenv
import requests
from config import APIKEY

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '!')

def weather(city):
    api_call = f'http://api.openweathermap.org/data/2.5/weather?q={city}&apid={APIKEY}'
    r = requests.get(api_call)
    return r.json()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command('temp')
async def temp(ctx):
    weather_result = weather('Kingwood')
    await ctx.send(weather_result)
    await ctx.send('hello')

bot.run(TOKEN)