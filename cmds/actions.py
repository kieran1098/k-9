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

class actions(commands.Cog):

   def __init__(self,client):
    self.client = client
  
    
   @commands.command (aliases=['Punch' , 'PUNCH'], help="ping a user to punch")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def punch (self, ctx, arg1):

       Punch_Phrases = [
         f'***{ctx.author}*** Delivered a fatal Blow to **{arg1}**',
         f'**{arg1}** got their face crushed by ***{ctx.author}***',
         f"***{ctx.author}*** destroyed **{arg1}'s** Face ",
         f'***{ctx.author}*** killed **{arg1}** with a hellish punch'
       ]

       Punch_GIFS = [
         'https://tenor.com/view/kirby-punch-stuffed-toy-beat-up-gif-17938642',
         'https://tenor.com/view/beating-up-beating-up-lilo-fight-beat-up-beat-down-gif-19482217',
         'https://tenor.com/view/cat-cute-adorable-punch-gif-17822730',
         'https://tenor.com/view/bugs-bunny-punch-spin-gif-12060927',
         'https://tenor.com/view/asdfmovie-theres-something-on-your-face-it-was-pain-pain-punch-gif-21774667'
       ]
       await ctx.send(random.choice(Punch_Phrases))
       await ctx.send(random.choice (Punch_GIFS))

   @punch.error
   async def punch_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to punch, punch yourself for that one!", color=0xb9b9b9)
        await ctx.send(embed=embed)

   @punch.error
   async def punch_error2(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


   @commands.command (aliases=['kiss' , 'KISS'], help="ping a user to kiss")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Kiss (self, ctx, arg1):

       Kiss_Phrases = [
         f'***{ctx.author}*** kisses **{arg1}** OWO',
         f'**{ctx.author}** kisses ***{arg1}***',
         f"***{ctx.author}*** smooches **{arg1}'s** Face "
       ]

       Kiss_GIFS = [
         'https://tenor.com/view/kiss-a-homie-kiss-smack-gif-17593938',
         'https://tenor.com/view/black-guys-kissing-2homies-being-homies-mwah-gif-16687510',
         'https://tenor.com/view/ripz-kiss-kissahomie-roflgator-chipz-gif-19747597',
         'https://tenor.com/view/surrender-kiss-anime-gay-kisses-gif-7301675',
         'https://tenor.com/view/anime-kiss-love-sweet-gif-5095865'
       ]
       await ctx.send(random.choice(Kiss_Phrases))
       await ctx.send(random.choice (Kiss_GIFS))

   @Kiss.error
   async def kiss_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to kiss, punch yourself for that one!", color=0xb9b9b9)
        await ctx.send(embed=embed)

   @Kiss.error
   async def kiss_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


   @commands.command (aliases=['hug' , 'HUG'], help="ping a user to hug")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Hug (self, ctx, arg1):

       Hug_Phrases = [
          f'***{ctx.author}*** hugs **{arg1}** OWO',
          f'**{ctx.author}** hugs ***{arg1}***',
          f"***{ctx.author}*** cuddles **{arg1}'s** "
      ]

       Hug_GIFS = [
         'https://tenor.com/view/cat-love-huge-hug-big-gif-11990658',
         'https://tenor.com/view/otters-sea-hug-sweet-finding-dory-gif-13642193',
         'https://tenor.com/view/love-cats-cat-cute-hug-love-gif-16191958',
         'https://tenor.com/view/couple-hug-love-sweet-gif-7880177',
         'https://tenor.com/view/huge-hug-bromance-cute-dog-dog-love-love-you-gif-15055257'
       ]
       await ctx.send(random.choice(Hug_Phrases))
       await ctx.send(random.choice (Hug_GIFS))

   @Hug.error
   async def hug_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to hug, punch yourself for that one!", color=0xb9b9b9)
        await ctx.send(embed=embed)
   
   @Hug.error
   async def Hug_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)

   @commands.command (aliases=['kill' , 'KILL'], help="ping a user to kill")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Kill (self, ctx, arg1):

       Kill_Phrases = [
          f'***{ctx.author}*** assaulted **{arg1}**',
          f'**{ctx.author}** killed ***{arg1}***',
          f"***{ctx.author}*** murdered **{arg1}** "
      ]

       Kill_GIFS = [
         'https://tenor.com/view/killed-em-hold-this-stabbed-gif-14017151',
         'https://tenor.com/view/kill-you-sailor-moon-cant-breathe-gif-15062996',
         'https://tenor.com/view/among-us-kill-gif-19295404',
         'https://tenor.com/view/kill-you-strangle-gif-10414382',
         'https://tenor.com/view/shoot-kill-bullet-gif-18649705'
       ]
       await ctx.send(random.choice(Kill_Phrases))
       await ctx.send(random.choice (Kill_GIFS))

   @Kill.error
   async def Kill_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to hug, punch yourself for that one!", color=0xb9b9b9)
        await ctx.send(embed=embed)

   @Kill.error
   async def Kill_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)
      


   @commands.command (aliases=['bully' , 'BULLY'], help="ping a user to bully")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Bully (self, ctx, arg1):

       Bully_Phrases = [
          f'***{ctx.author}*** assaulted **{arg1}**',
          f'**{ctx.author}** pushed around ***{arg1}***',
          f"***{ctx.author}*** tormented **{arg1}** "
      ]

       Bully_GIFS = [
         'https://tenor.com/view/short-paws-rude-cat-bully-gif-19631347',
         'https://tenor.com/view/throwing-gif-20173152',
         'https://tenor.com/view/bully-soccer-gif-9249976',
         'https://tenor.com/view/bully-surprise-penguin-gif-16323347',
         'https://tenor.com/view/kitten-cute-adorable-cat-bully-gif-15622607'
         
       ]
       await ctx.send(random.choice(Bully_Phrases))
       await ctx.send(random.choice (Bully_GIFS))

   @Bully.error
   async def Bully_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to bully, punch yourself for that one!", color=0xb9b9b9)
        await ctx.send(embed=embed)

   @Bully.error
   async def Bully_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)



   @commands.command (aliases=['wave' , 'WAVE'], help="ping a user to wave at")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Wave (self, ctx, arg1):

       Wave_Phrases = [
          f'***{ctx.author}*** waved at **{arg1}**',
          f'**{ctx.author}** greated ***{arg1}***'
      ]

       Wave_GIFS = [
         'https://tenor.com/view/forest-gump-wave-hi-hello-howdy-gif-22164679',
         'https://tenor.com/view/mr-bean-wave-hi-gif-8704755',
         'https://tenor.com/view/stephen-king-it-pennywise-clown-wave-gif-17272084',
         'https://tenor.com/view/hello-hey-wave-bear-hi-gif-5859657',
         'https://tenor.com/view/fred-flintstone-the-flintstones-surfing-surfs-up-waves-hello-gif-18972368'
       ]
       await ctx.send(random.choice(Wave_Phrases))
       await ctx.send(random.choice (Wave_GIFS))

   @Wave.error
   async def Wave_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to wave at, punch yourself for that one!", color=0xb9b9b9)
        await ctx.send(embed=embed)

   @Wave.error
   async def Wave_err(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
        await ctx.send(embed=embed)


   @commands.command (aliases=['lick' , 'LICK'], help="ping a user to lick")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Lick(self, ctx, arg1):

       Lick_Phrases = [
          f'***{ctx.author}*** licked **{arg1}**',
      ]

       Lick_GIFS = [
         'https://tenor.com/view/stitch-lick-saliva-gif-5509072',
         'https://tenor.com/view/eat-out-eating-out-reaction-mrw-reactions-gif-5036759',
         'https://tenor.com/view/lick-cat-lick-cat-cute-gif-20170312',
         'https://tenor.com/view/cat-lick-kiss-me-you-gif-15778247',
         'https://tenor.com/view/weird-hungry-finding-food-dog-licking-couch-starving-gif-14558017'
         
       ]
       await ctx.send(random.choice(Lick_Phrases))
       await ctx.send(random.choice (Lick_GIFS))

   @Lick.error
   async def Lick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to lick, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Lick.error
   async def Lick_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)

   @commands.command (aliases=['pat' , 'PAT'], help="ping a user to pat")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Pat(self, ctx, arg1):

       Pat_Phrases = [
          f'***{ctx.author}*** patted **{arg1}**',
      ]

       Pat_GIFS = [
         'https://tenor.com/view/good-boy-pat-on-head-stitch-gif-14742401',
         'https://tenor.com/view/big-hero6-baymax-there-there-patting-head-pat-head-gif-4086973',
         'https://tenor.com/view/bunny-too-cute-adorable-head-pat-cute-gif-17246426',
         'https://tenor.com/view/funny-dog-cat-patting-head-gif-4953911',
         'https://tenor.com/view/rub-kitty-cute-kitty-pat-kitty-cat-cattow-gif-21375767'
         
       ]
       await ctx.send(random.choice(Pat_Phrases))
       await ctx.send(random.choice (Pat_GIFS))

   @Pat.error
   async def Pat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to pat, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Pat.error
   async def Pat_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)

   @commands.command (aliases=['slap' , 'SLAP'], help="ping a user to SLAP")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Slap(self, ctx, arg1):

       Slap_Phrases = [
          f'***{ctx.author}*** slapped **{arg1}**',
          f'***{ctx.author}*** assaulted **{arg1}**',
      ]

       Slap_GIFS = [
         'https://tenor.com/view/slap-in-the-face-angry-gtfo-bitc-bitch-slap-gif-15667197',
         'https://tenor.com/view/slap-annoyed-irritated-kid-gif-5013065',
         'https://tenor.com/view/batman-slap-robin-slap-gif-10206784',
         'https://tenor.com/view/spongebob-squarepants-patrick-star-gloves-slap-gif-17514643',
         'https://tenor.com/view/back-slap-backhand-funny-animals-penguin-slap-gif-11724800'
         
       ]
       await ctx.send(random.choice(Slap_Phrases))
       await ctx.send(random.choice (Slap_GIFS))

   @Slap.error
   async def Slap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to slap, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Slap.error
   async def Slap_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)   


   @commands.command (aliases=['tickle' , 'TICKLE'], help="ping a user to tickle")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Tickle(self, ctx, arg1):

       Tickle_Phrases = [
          f'***{ctx.author}*** tickled **{arg1}**',
          f'***{ctx.author}*** touched **{arg1}**',
      ]

       Tickle_GIFS = [
         'https://tenor.com/view/cosquillas-risa-jugando-riendo-jaja-gif-16433239',
         'https://tenor.com/view/gif-gif-19493511',
         'https://tenor.com/view/super-troopers-feather-tickle-gif-22411184',
         'https://tenor.com/view/tickle-dog-gif-19755745',
         'https://tenor.com/view/shark-baby-shark-gif-21792225'
         
       ]
       await ctx.send(random.choice(Tickle_Phrases))
       await ctx.send(random.choice (Tickle_GIFS))

   @Tickle.error
   async def Tickle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to tickle, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Tickle.error
   async def Tickle_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)      


   @commands.command (aliases=['bite' , 'BITE'], help="ping a user to BITE")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Bite(self, ctx, arg1):

       Bite_Phrases = [
          f'***{ctx.author}*** bit **{arg1}**',
          f'***{ctx.author}*** ate **{arg1}**',
      ]

       Bite_GIFS = [
         'https://tenor.com/view/rip-bite-cat-kitty-pet-gif-17924889',
         'https://tenor.com/view/josee-josee-to-tora-to-sakanatachi-bite-girl-tsuneo-gif-20061862',
         'https://tenor.com/view/spongebob-wacky-bite-got-me-gif-16950691',
         'https://tenor.com/view/cat-finger-bite-cat-finger-bite-cat-bite-gif-21471247',
         'https://tenor.com/view/cat-kitten-attack-mitsou-adorable-gif-17755857'
         
       ]
       await ctx.send(random.choice(Bite_Phrases))
       await ctx.send(random.choice (Bite_GIFS))

   @Bite.error
   async def Bite_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to bite, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Bite.error
   async def Bite_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)      


   @commands.command (aliases=['poke' , 'POKE'], help="ping a user to poke")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Poke(self, ctx, arg1):

       Poke_Phrases = [
          f'***{ctx.author}*** pokked **{arg1}**',
          f'***{ctx.author}*** touched **{arg1}**',
      ]

       Poke_GIFS = [
         'https://tenor.com/view/bird-cute-poke-sweet-gif-16818145',
         'https://tenor.com/view/viralhog-cat-blank-stare-focused-forgot-how-to-cat-gif-11710639',
         'https://tenor.com/view/pillsbury-doughboy-poke-poking-cute-gif-16694531',
         'https://tenor.com/view/poke-dog-baby-gif-12780689',
         'https://tenor.com/view/h%C3%A1mster-susto-miedo-surprised-shocked-gif-17225118'
         
       ]
       await ctx.send(random.choice(Poke_Phrases))
       await ctx.send(random.choice (Poke_GIFS))

   @Poke.error
   async def Poke_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to poke, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Poke.error
   async def Poke_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)   


   @commands.command (aliases=['bonk' , 'BONK'], help="ping a user to bonk")
   @commands.cooldown(1,5,commands.BucketType.user)
   async def Bonk(self, ctx, arg1):

       Bonk_Phrases = [
          f'***{ctx.author}*** bonked **{arg1}**',
          f'***{ctx.author}*** hit **{arg1}**',
      ]

       Bonk_GIFS = [
         'https://tenor.com/view/kendo-shinai-bonk-doge-horny-gif-20995284',
         'https://tenor.com/view/bonk-gif-19410756',
         'https://tenor.com/view/guillotine-bonk-revolution-gif-20305805',
         'https://tenor.com/view/bonk-dog-smash-gif-16816642',
         'https://tenor.com/view/walter-bonk-walter-bonk-nelson-dog-gif-15721111'
         
       ]
       await ctx.send(random.choice(Bonk_Phrases))
       await ctx.send(random.choice (Bonk_GIFS))

   @Bonk.error
   async def Bonk_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
          embed = discord. Embed(title="Wait a minute!", description="You forgot to mention someone to bonk, punch yourself for that one!", color=0xb9b9b9)
          await ctx.send(embed=embed)

   @Bonk.error
   async def Bonk_err(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
          embed = discord.Embed(title='Slow down!', description='this command is on cooldown' , color=0xb9b9b9)
          await ctx.send(embed=embed)     
  

    
  

def setup(client):
  client.add_cog(actions(client))
