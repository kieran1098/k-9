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


class animals(commands.Cog):
   def __init__(self, client):
        self.client = client

   @commands.command(aliases=['doge', 'DOGE', 'dog', 'DOG'])
   async def Dog(self, ctx):
        complete_url = 'https://dog.ceo/api/breeds/image/random'

        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No dog found :(')

                x = await response.json()

                embed = discord.Embed(title='Random Dog',
                                      color=0xb9b9b9,
                                      timestamp=ctx.message.created_at)
                embed.set_image(url=x['message'])

                await ctx.send(embed=embed)

   @Dog.error
   async def Dog_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


   @commands.command(aliases=['cat', 'CAT', 'pussy', 'PUSSY'])
   async def Cat(self, ctx):
        complete_url = 'https://api.thecatapi.com/v1/images/search'

        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No cat found :(')

                x = await response.json()

                embed = discord.Embed(title='Random Cat',
                                      color=0xb9b9b9,
                                      timestamp=ctx.message.created_at)
                embed.set_image(url=x[0]['url'])

                await ctx.send(embed=embed)

   @Cat.error
   async def Cat_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.cooldown(1,3,commands.BucketType.user)
   @commands.command(aliases=['Bird','BIRD'])
   async def bird(self, ctx):
    Bird = [
      'random bird',
      
    ]
    async with aiohttp.ClientSession() as a:
      async with a.get("https://some-random-api.ml/img/birb") as b:
        c = await b.json() 



        embed = discord.Embed(
          title=(random.choice(Bird)),
          description=" ",
          color=0xb9b9b9,
        
          
        )
        embed.set_image(url=c['link'])
        await ctx.send(embed=embed)

   @bird.error
   async def bird_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.cooldown(1,3,commands.BucketType.user)
   @commands.command(aliases=['panda','PANDA'])
   async def Panda(self, ctx):
    panda = [
      'random panda',
      
    ]
    async with aiohttp.ClientSession() as a:
      async with a.get("https://some-random-api.ml/img/panda") as b:
        c = await b.json() 



        embed = discord.Embed(
          title=(random.choice(panda)),
          description=" ",
          color=0xb9b9b9,
        
          
        )
        embed.set_image(url=c['link'])
        await ctx.send(embed=embed)

   @Panda.error
   async def Panda_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.cooldown(1,3,commands.BucketType.user)
   @commands.command(aliases=['redpanda','REDPANDA'])
   async def RedPanda(self, ctx):
      redpanda = [
      'random redpanda',
      
      ]
      async with aiohttp.ClientSession() as a:
        async with a.get("https://some-random-api.ml/img/red_panda") as b:
          c = await b.json() 



          embed = discord.Embed(
            title=(random.choice(redpanda)),
            description=" ",
            color=0xb9b9b9,
        
          
          )
          embed.set_image(url=c['link'])
          await ctx.send(embed=embed)

   @RedPanda.error
   async def RedPanda_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.cooldown(1,3,commands.BucketType.user)
   @commands.command(aliases=['fox','FOX'])
   async def Fox(self, ctx):
      fox = [
      'random Fox',
      
      ]
      async with aiohttp.ClientSession() as a:
        async with a.get("https://some-random-api.ml/img/fox") as b:
          c = await b.json() 



          embed = discord.Embed(
            title=(random.choice(fox)),
            description=" ",
            color=0xb9b9b9,
        
          
          )
          embed.set_image(url=c['link'])
          await ctx.send(embed=embed)   
    
   @Fox.error
   async def Fox_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.cooldown(1,3,commands.BucketType.user)
   @commands.command(aliases=['koala','KOALA'])
   async def Koala(self, ctx):
      koala = [
      'random koala',
      
      ]
      async with aiohttp.ClientSession() as a:
        async with a.get("https://some-random-api.ml/img/koala") as b:
          c = await b.json() 



          embed = discord.Embed(
            title=(random.choice(koala)),
            description=" ",
            color=0xb9b9b9,
        
          
          )
          embed.set_image(url=c['link'])
          await ctx.send(embed=embed)      

   @Koala.error
   async def Koala_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


def setup(client):
  client.add_cog(animals(client))