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

class emotes(commands.Cog):

   def __init__(self,client):
    self.client = client

   @commands.command (aliases=['happy' , 'HAPPY'], help="send a happy gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Happy (self, ctx,):

       Happy_Phrases = [
          f'***{ctx.author}*** smiled',
          f'**{ctx.author}** is happy'
      ]

       Happy_GIFS = [
         'https://tenor.com/view/xmas-happy-dance-gif-13017096',
         'https://tenor.com/view/tom-hanks-surprised-happy-shocked-gif-3685548',
         'https://tenor.com/view/dance-happy-food-gettin-it-getting-hype-gif-10970905',
         'https://tenor.com/view/happy-dance-excited-crazy-tutu-gif-4867955',
         'https://tenor.com/view/bailar-dance-happy-tom-and-jerry-gif-14081211'
       ]
       await ctx.send(random.choice(Happy_Phrases))
       await ctx.send(random.choice (Happy_GIFS))

   @Happy.error
   async def happy_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

 

   @commands.command (aliases=['sad' , 'SAD'], help="send a sad gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Sad (self, ctx,):

       Sad_Phrases = [
          f'***{ctx.author}*** cried',
          f'***{ctx.author}*** is sad',
          f'***{ctx.author}*** is depressed'
      ]

       Sad_GIFS = [
         'https://tenor.com/view/sad-eyes-so-sad-tears-gif-13901135',
         'https://tenor.com/view/sad-baby-frown-cry-tantrums-gif-4649018',
         'https://tenor.com/view/pout-girl-sad-cry-little-girl-gif-20041802',
         'https://tenor.com/view/sad-walk-of-shame-shame-shameful-head-down-gif-5548725',
         'https://tenor.com/view/the-office-crying-michael-scott-sad-upset-gif-9816214'
       ]
       await ctx.send(random.choice(Sad_Phrases))
       await ctx.send(random.choice (Sad_GIFS))

   @Sad.error
   async def Sad_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   
   @commands.command (aliases=['blush' , 'BLUSH'], help="send a blushing gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Blush (self, ctx,):

       Blush_Phrases = [
          f'***{ctx.author}*** blushed',
          f'**{ctx.author}** is blushing'
      ]

       Blush_GIFS = [
         'https://tenor.com/view/joey-tribbiani-friends-smile-ramzes19-scromnyaga-gif-12180398',
         'https://tenor.com/view/janhvi-janhvi-kapoor-sweet-thats-so-sweet-cute-gif-20831172',
         'https://tenor.com/view/shy-bashful-flirt-smile-smirk-gif-13064653',
         'https://tenor.com/view/goofy-gif-8102686',
         'https://tenor.com/view/tom-and-jerry-tom-blushing-shy-blush-gif-20367454'
       ]
       await ctx.send(random.choice(Blush_Phrases))
       await ctx.send(random.choice (Blush_GIFS))

   @Blush.error
   async def Blush_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


   @commands.command (aliases=['cry' , 'CRY'], help="send a crying gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Cry (self, ctx,):

       Cry_Phrases = [
          f'***{ctx.author}*** cried',
          f'**{ctx.author}** is crying'
      ]

       Cry_GIFS = [
         'https://tenor.com/view/sad-cry-crying-tears-broken-gif-15062040',
         'https://tenor.com/view/tom-y-jerry-tom-and-jerry-meme-sad-cry-gif-18054267',
         'https://tenor.com/view/cat-catcry-gif-19131995',
         'https://tenor.com/view/pepe-why-pepe-the-frog-sad-crying-gif-16026853',
         'https://tenor.com/view/sadgecry-bttv-twitch-gif-22954193'
       ]
       await ctx.send(random.choice(Cry_Phrases))
       await ctx.send(random.choice (Cry_GIFS))

   @Cry.error
   async def Cry_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['mad' , 'MAD'], help="send a angry gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Mad (self, ctx,):

       Mad_Phrases = [
          f'***{ctx.author}*** is angry',
          f'**{ctx.author}** is mad'
      ]

       Mad_GIFS = [
         'https://tenor.com/view/angry-anger-pixar-inside-out-aaah-gif-5628546',
         'https://tenor.com/view/angry-kid-vine-table-tantrums-gif-9382123',
         'https://tenor.com/view/mad-mad-face-pissed-frustrated-frustration-gif-15931246',
         'https://tenor.com/view/angry-andre-sitolini-engetic-butthurt-gif-14985012',
         'https://tenor.com/view/angry-bubbles-bubbles-fire-furious-mad-gif-12674420'
       ]
       await ctx.send(random.choice(Mad_Phrases))
       await ctx.send(random.choice (Mad_GIFS))

   @Mad.error
   async def Mad_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['problem' , 'PROBLEM'], help="send a trolling gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Problem (self, ctx,):

       Problem_Phrases = [
          f'***{ctx.author}*** is trolling',
          f'**{ctx.author}** is doing a lil trolling'
      ]

       Problem_GIFS = [
         'https://tenor.com/view/meme-troll-drive-by-memes-gif-18645179',
         'https://tenor.com/view/trolling-gif-21943469',
         'https://tenor.com/view/troll-dance-captain-gif-4494681',
         'https://tenor.com/view/troll-face-slap-smile-gif-15260095',
         'https://tenor.com/view/trol-we-do-a-little-trolling-we-do-a-little-tomfoolery-we-do-a-little-bit-of-trolling-troll-gif-23734601'
       ]
       await ctx.send(random.choice(Problem_Phrases))
       await ctx.send(random.choice (Problem_GIFS))

   @Problem.error
   async def Problem_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


   @commands.command (aliases=['bruh' , 'BRUH'], help="send a bruh gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Bruh (self, ctx,):

       Bruh_Phrases = [
          f'***{ctx.author}*** is tired of your shit',
          f'**{ctx.author}** is sighing'
      ]

       Bruh_GIFS = [
         'https://tenor.com/view/bruh-moment-gif-23616422',
         'https://tenor.com/view/really-bruh-blink-blank-face-gif-12917060',
         'https://tenor.com/view/bruh-gif-22596911',
         'https://tenor.com/view/bruh-gif-18669243',
         'https://tenor.com/view/bruh-moment-bruh-moment-recording-gif-14698316'
       ]
       await ctx.send(random.choice(Bruh_Phrases))
       await ctx.send(random.choice (Bruh_GIFS))

   @Bruh.error
   async def Bruh_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['shrug' , 'SHRUG'], help="send a shrug gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Shrug(self, ctx,):

       Shrug_Phrases = [
          f'***{ctx.author}*** shrugged',
          f'**{ctx.author}** is confused'
      ]

       Shrug_GIFS = [
         'https://tenor.com/view/say-what-dunno-shrug-john-krasinski-idk-gif-16557956',
         'https://tenor.com/view/really-shrug-seriously-james-little-james-gif-11213198',
         'https://tenor.com/view/emotions-reactions-trump-yes-oh-well-gif-7774956',
         'https://tenor.com/view/elmo-shrug-%E4%B8%8D%E9%80%A0-i-dont-know-gif-5094560',
         'https://tenor.com/view/shrug-jakethedog-adventuretime-idunno-idk-gif-7391243'
       ]
       await ctx.send(random.choice(Shrug_Phrases))
       await ctx.send(random.choice (Shrug_GIFS))

   @Shrug.error
   async def Shrug_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['sleepy' , 'SLEEPY'], help="send a sleepy gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Sleep(self, ctx,):

       Sleep_Phrases = [
          f'***{ctx.author}*** is sleepy',
          f'**{ctx.author}** is tired'
      ]

       Sleep_GIFS = [
         'https://tenor.com/view/cat-sleep-tired-cute-fall-gif-17673985',
         'https://tenor.com/view/sushichaeng-reaction-tired-tired-af-sleepy-gif-21021085',
         'https://tenor.com/view/japa-sleep-sleepy-gif-21232217',
         'https://tenor.com/view/sleep-sleeping-time-tom-and-jerry-mouse-rat-gif-16820940',
         'https://tenor.com/view/sleepy-friends-gif-9758438'
       ]
       await ctx.send(random.choice(Sleep_Phrases))
       await ctx.send(random.choice (Sleep_GIFS))

   @Sleep.error
   async def Sleep_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['smug' , 'SMUG'], help="send a smug gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Smug(self, ctx,):

       Smug_Phrases = [
          f'***{ctx.author}*** is smug',
          f'**{ctx.author}** is showing off'
      ]

       Smug_GIFS = [
         'https://tenor.com/view/top-gun-tom-cruise-sunglasses-smile-fuck-yea-gif-3684204',
         'https://tenor.com/view/jeremy-clarkson-top-gear-smug-driving-gif-13545678',
         'https://tenor.com/view/smirk-spongebob-spongebob-squarepants-silly-smile-gif-4953511',
         'https://tenor.com/view/mcgregor-cocky-smug-ufc-gif-9584477',
         'https://tenor.com/view/hmm-jeff-goldblum-smirk-evil-smile-snigger-gif-15631044'
       ]
       await ctx.send(random.choice(Smug_Phrases))
       await ctx.send(random.choice (Smug_GIFS))

   @Smug.error
   async def Smug_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['thinking' , 'THINKING'], help="send a thinking gif")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Thinking(self, ctx,):

       Thinking_Phrases = [
          f'***{ctx.author}*** is thinking',
          f'**{ctx.author}** is having a big brain moment'
      ]

       Thinking_GIFS = [
         'https://tenor.com/view/hmm-spongebob-meme-think-gif-15884400',
         'https://tenor.com/view/math-thinking-zach-galifianakis-formulas-numbers-gif-7715569',
         'https://tenor.com/view/confused-math-what-wtf-peep-gif-6081931',
         'https://tenor.com/view/thinking-tap-spongebob-spongebob-squarepants-contemplate-gif-5837190',
         'https://tenor.com/view/batman-thinking-contemplating-pondering-chin-gif-4540781'
       ]
       await ctx.send(random.choice(Thinking_Phrases))
       await ctx.send(random.choice (Thinking_GIFS))

   @Thinking.error
   async def Thinking_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


def setup(client):
  client.add_cog(emotes(client))