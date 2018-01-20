import discord
from discord.ext import commands
import json
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet():
    await bot.say('hello')

bot.run(config['discord_key'])