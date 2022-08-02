import discord
import xkcd
import copy
from PIL import Image, ImageFilter
from asyncdagpi import Client, ImageFeatures
import blissops as imageops
import os
from random import sample
import asyncio
import time
import ksoftapi
import emoji
import json
from googletrans import Translator, LANGUAGES
from textwrap import TextWrapper
from youtube_dl import YoutubeDL
import box
from random import shuffle
import string
from enum import Enum
import random
import sys
from urllib.parse import quote_plus
from collections import deque
import aiohttp
import numpy
import requests
from discord.ext.commands import clean_content
import traceback
import hashlib
from random import choice
from discord.ext import commands
from xo import ai
from xo.game import Game
from discord.ext.commands import Bot
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup

class help(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.command(aliases = ["help", "HELP"])
  @commands.cooldown(1,5,commands.BucketType.user)
  async def Help(self, ctx):
         embed = discord.Embed(title = 'Help for K-9', description='All bot commands here: \n need more help? join our server [HERE](https://discord.gg/zusJCrpNKQ)', color=0xb9b9b9)
         embed.add_field(name='**:musical_note: MUSIC**', value='``play``, ``pause``, ``resume``, ``skip``, ``queue``, ``disconnect``', inline=False)
         embed.add_field(name=':game_die:**GAMES**', value='``blackjack``, ``hilo``', inline=False)
         embed.add_field(name='**:8ball: FUN**', value='``meme``, ``8ball [question]``, ``coinflip``, ``rolldice``, ``pp``, ``gym-tips``, ``fact``, ``gayrate [ping]``, ``quote``, ``facereveal [ping]``', inline=False)
         embed.add_field(name='**:dog: ANIMALS**', value='``dog``, ``cat``, ``bird``,``panda``, ``redpanda``, ``fox``, ``koala``', inline=False)
         embed.add_field(name='**:slight_smile: EMOTES**', value='``happy``, ``sad``, ``blush``, ``cry``, ``mad``, ``problem``, ``bruh``, ``shrug``, ``sleepy``, ``smug``, ``thinking``', inline=False)
         embed.add_field(name='**:hugging: ACTIONS [ping]**', value='``punch``, ``kiss``, ``hug``, ``kill``, ``bully``, ``wave``, ``lick``, ``pat``, ``slap``, ``tickle``, ``bite``, ``poke``, ``bonk``', inline=False)
         embed.add_field(name='**:camera: FILTERS WORK IN PROGRESS**', value='``horny``, ``arrest``, ``trigger``, ``gay``, ``wasted``', inline=False)
         embed.add_field(name='**:tools: MODERATION**', value='``ban``, ``kick``, ``mute``, ``unmute``, ``purge`` ', inline=False)
         embed.add_field(name='**:wrench: EXTRA**', value='``ping``, ``invite``, ``serverinvite``, ``patreon``, ``whois``, ``serverinfo``, ``ip [ip]``, ``guildcount``', inline=False)
         embed.set_footer(text='Bot developed by Bri ish Spy')
         embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9f30dc2c-be55-4f3c-afed-6655411ba634/d9u29hh-4a973fa7-26da-4079-86b5-76c308da6e39.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzlmMzBkYzJjLWJlNTUtNGYzYy1hZmVkLTY2NTU0MTFiYTYzNFwvZDl1MjloaC00YTk3M2ZhNy0yNmRhLTQwNzktODZiNS03NmMzMDhkYTZlMzkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.-PR_W8izeoC1B-2waAIpzP9jhF8jjRtZtrS1Al4xWdY')
         embed.set_image(url='')
         await ctx.send(embed=embed)


  @Help.error
  async def Help_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)





def setup(client):
  client.add_cog(help(client))
