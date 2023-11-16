import discord
from discord.ext import commands 
import asyncio 
from random import choices, randint # lib to pick a random number between a and b
client = commands.Bot(command_prefix='/', intents=discord.Intents.default())

@client.event 
async def on_ready(): # When the bot is online
    print("Bot Ready !")
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = "avec sanic !")) # "Listening to Cool Music !" < in status


client.run("")
