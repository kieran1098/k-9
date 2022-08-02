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
import datetime
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

class extra(commands.Cog):
     
   def __init__(self,client):
    self.client = client  

   @commands.command(name="ping", help="shows ping between user and bot")
   async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.client.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

   @commands.command(aliases=['invite', 'INVITE'], help="sends bot invite link")
   async def Invite(self, ctx):
         myembed = discord.Embed(title = 'DISCORD BOT INVITE', description='click [HERE](https://discord.com/api/oauth2/authorize?client_id=910200576153911326&permissions=8&scope=bot) to invite my bot')
         await ctx.send(embed=myembed)


   @commands.command(aliases=['serverinvite', 'SERVERINVITE'], help="discord server invite link")
   async def ServerInvite(self, ctx):
         myembed = discord.Embed(title = 'SERVER INVITE', description='click [HERE](https://discord.gg/zusJCrpNKQ) to join my discord server')
         await ctx.send(embed=myembed)


   @commands.command(aliases=['patreon', 'PATREON'], help="sends patreon link")
   async def Patreon(self, ctx):
         myembed = discord.Embed(title = 'PATREON LINK', description='click [HERE](https://www.patreon.com/BriishSpy) for my patreon link')
         await ctx.send(embed=myembed)

   @commands.command(aliases=['whois' , 'WHOIS'])
   async def Whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        roles = [role for role in member.roles[1:]]

        embed = discord.Embed(color=0xb9b9b9, timestamp=ctx.message.created_at, title=f'User Info - {member}')

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}')

        embed.add_field(name='ID: ', value=member.id, inline=False)
        embed.add_field(name='Display Name: ', value=member.display_name, inline=False)
        embed.add_field(name='Created Account On: ', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        await ctx.send(embed=embed)

   @commands.is_owner()
   @commands.command()
   async def pull(self, ctx, guild_id: int):
        guild = self.client.get_guild(guild_id)
        guildchannel = guild.system_channel
        invitelink = await guildchannel.create_invite(max_uses=100, unique=True)
        await ctx.author.send(invitelink)


   @commands.is_owner()
   @commands.command()
   async def pullnames(self, ctx):
        activeserver = self.client.guilds

        for guild in activeserver:
            await ctx.send(f"Guild Name: {guild.name} \nGuild ID: {guild.id}\nGuild Owner: {guild.owner}\n------")

   @commands.cooldown(1,3,commands.BucketType.user)
   @commands.command(name="ServerInfo", aliases=['serverinfo', 'SINFO', 'sinfo'])
   async def Serverinfo(self, ctx):
     await ctx.trigger_typing()
     owner = str(ctx.guild.owner)

     embed = discord.Embed(
       title=f"Info for guild: {ctx.guild}",
       description=f"Guild ID: {ctx.guild.id}",
       color=0xb9b9b9,
       timestamp = datetime.datetime.utcnow())
     embed.add_field(
       name=f"Owner: ",
       value=owner,
       inline=False)


     embed.add_field(
       name=f"Member Count: ",
       value=f"{ctx.guild.member_count}",
       inline=False)

     embed.add_field(
       name="Roles",
       value=f"{len(ctx.guild.roles)}",
       inline=False)


     embed.add_field(
       name="Guild emojis",
       value=f"{len(ctx.guild.emojis)}"
     )



     embed.add_field(
       name="Server Prefix",
       value=f"{ctx.prefix}",
       inline=False
     )
     await ctx.send(embed=embed)
    
   @commands.command()
   async def guildcount(self, ctx):
     await ctx.trigger_typing()
		

     await ctx.send(f"K-9 is in {len(self.client.guilds)} guilds.")

   @commands.cooldown(1,20,commands.BucketType.user)
   @commands.command(name="iplookup", aliases=['ip', 'ipl'])
   async def iplookup(self, ctx, *, ip):
    async with aiohttp.ClientSession() as a:
      async with a.get(f"http://ipwhois.app/json/{ip}") as b:
        c = await b.json()

        try:
					
          coordj = ''.join(f"{c['latitude']}" + ", " + f"{c['longitude']}")
          embed = discord.Embed(
          title="IP: {}".format(ip),
						description=f"```txt\n\nLocation Info:\nIP: {ip}\nIP Type: {c['type']}\nCountry, Country code: {c['country']} ({c['country_code']})\nPhone Number Prefix: {c['country_phone']}\nRegion: {c['region']}\nCity: {c['city']}\nCapital: {c['country_capital']}\nLatitude: {c['latitude']}\nLongitude: {c['longitude']}\nLat/Long: {coordj} \n\nTimezone Info:\nTimezone: {c['timezone']}\nTimezone Name: {c['timezone_name']}\nTimezone (GMT): {c['timezone_gmt']}\nTimezone (GMT) offset: {c['timezone_gmtOffset']}\n\nContractor/Hosting Info:\nASN: {c['asn']}\nISP: {c['isp']}\nORG: {c['org']}\n\nCurrency:\nCurrency type: {c['currency']}\nCurrency Code: {c['currency_code']}\nCurrency Symbol: {c['currency_symbol']}\nCurrency rates: {c['currency_rates']}\nCurrency type (plural): {c['currency_plural']}```",
						color=0xb9b9b9
					)
          embed.set_footer(text="Made using the https://ipwhois.io/ API.")
					
					
					
          await ctx.send(embed=embed)
					
					
        except KeyError:
         await ctx.send("KeyError has occured, perhaps this is a bogon IP address, or invalid IP address?")


def setup(client):
  client.add_cog(extra(client))
