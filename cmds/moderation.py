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

class mod(commands.Cog):

   def __init__(self,client):
    self.client = client

   @commands.command(aliases=["ban", "BAN"])
   @commands.has_permissions(ban_members=True)
   async def Ban(self, ctx, member: discord.Member, *, reason=None):
         await member.ban(reason=reason)
         await ctx.send(f'``User {member} has been banned``')

   @commands.command(aliases=["kick", "KICK"])
   @commands.has_permissions(kick_members=True)
   async def Kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'``User {member} has been kicked``')

   @commands.command(aliases=['mute' , 'MUTE'])
   @commands.guild_only()
   @commands.has_permissions(manage_roles = True)
   async def Mute(self, ctx, member: discord.Member, reason = None):
        """
        Mutes a member.
        In order for this to work, the bot must have manage roles permissions.
        To use this command you must have manage roles permission.
        """

        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted is None:
            return await ctx.send(f'This server does not have a Muted role.')

        if member is ctx.author:
            return await ctx.send("Why are you trying to mute yourself?")

        await member.add_roles(muted)
        embed = discord.Embed(description = f'{member.mention} has been muted.', color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command(aliases=['unmute' , 'UNMUTE'])
   @commands.guild_only()
   @commands.has_permissions(manage_roles = True)
   async def Unmute(self, ctx, member: discord.Member):
        """
        Unmutes a member.
        In order for this to work, the bot must have manage roles permissions.
        To use this command you must have manage roles permission.
        """

        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted is None:
            return await ctx.send(f'This server does not have a Muted role.')

        if muted not in member.roles:
            return await ctx.send(f'{member.mention} is not muted.')

        await member.remove_roles(muted)
        embed = discord.Embed(description = f'{member.mention} has been unmuted.', color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command(aliases=['purge' , 'PURGE'])
   @commands.has_guild_permissions(manage_messages = True)
   async def Purge(self, ctx, amount = 0):
        """
        Clears specified number of messages.
        In order for this to work, the bot must have manage messages permissions.
        To use this command you must have manage messages permissions.
        """
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'Deleted {amount} messages.')
        await asyncio.sleep(5)
        await ctx.channel.purge(limit = 1)







def setup(client):
 client.add_cog(mod(client))
 