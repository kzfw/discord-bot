import discord
from discord.ext import commands
import os
import asyncio
import logging as log
import json
import datetime

# Setup Variables
TOKEN = os.getenv('DISCORD_TOKEN')
Intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents = Intents)
currentTime = str(datetime.datetime.now()).split(' ')[0]

# Logging Setup
log.basicConfig(
    filename='zfw-bot-%s.log' % currentTime,
    filemode='a',
    level=log.DEBUG, ### Change to INFO when releasing ###
    format='%(levelname)s:%(asctime)s:%(message)s'
)

# Body
@client.event
async def on_ready():
    log.info("Logged in as a bot {0.user}".format(client))
    print("Logged in as a bot {0.user}".format(client))

# TODO: Add Bot functions here...

# Run bot
client.run(TOKEN)