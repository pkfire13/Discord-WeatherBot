#weatherbot.py

import os
from discord.ext import commands
from dotenv import load_dotenv
import requests as r

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command('temp')
async def temp(ctx):
    await ctx.send('hello')

bot.run(TOKEN)