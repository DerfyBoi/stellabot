import json
import os
import platform
import random
import sys
import requests
from bs4 import BeautifulSoup
import asyncio

import discord
from discord.ext import tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('') #bot token ID redacted
GUILD = os.getenv('') #guild token ID redacted

bot = discord.Client()

#bot status
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#remove leading 0s
def format(code):
    global codeFormat
    codeFormat = code.lstrip("0")

#receive and format message if message is only a number
@bot.event
async def on_message(message):
    if message.content.isdecimal():
        code = message.content
        format(code)

        #opening website with number code
        url = "" + codeFormat #URL redacted
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        noscript = soup.find("picture")
        #scraping for image with img tag
        if noscript:
            img = noscript.find("img")
            if img:
                img_url = img['src']
                #sending image
                await message.channel.send(url)
                await message.channel.send(img_url)

bot.run('') #bot token ID redacted
