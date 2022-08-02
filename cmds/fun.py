import discord
import string
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


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rolldice", help="rolls a 6 sided dice")
    async def rolldice(self, ctx):
        """Roll some die"""
        await ctx.send("You rolled a {}!".format(random.randint(1, 6)))

    @commands.command(aliases=['8ball', '8BALL'])
    async def Eightball(self, ctx, *, _ballInput: clean_content):
        choiceType = random.choice(
            ["(Affirmative)", "(Non-committal)", "(Negative)"])
        if choiceType == "(Affirmative)":
            prediction = random.choice([
                "It is certain ", "It is decidedly so ", "Without a doubt ",
                "Yes, definitely ", "You may rely on it ", "As I see it, yes ",
                "Most likely ", "Outlook good ", "Yes ", "Signs point to yes "
            ]) + ":8ball:"

            emb = (discord.Embed(title="Question: {}".format(_ballInput),
                                 colour=0xb9b9b9,
                                 description=prediction))
        elif choiceType == "(Non-committal)":
            prediction = random.choice([
                "Reply hazy try again ", "Ask again later ",
                "Better not tell you now ", "Cannot predict now ",
                "Concentrate and ask again "
            ]) + ":8ball:"
            emb = (discord.Embed(title="Question: {}".format(_ballInput),
                                 colour=0xb9b9b9,
                                 description=prediction))
        elif choiceType == "(Negative)":
            prediction = random.choice([
                "Don't count on it ", "My reply is no ", "My sources say no ",
                "Outlook not so good ", "Very doubtful "
            ]) + ":8ball:"
            emb = (discord.Embed(title="Question: {}".format(_ballInput),
                                 colour=0xb9b9b9,
                                 description=prediction))
        emb.set_author(
            name='Magic 8 ball',
            icon_url=
            'https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png'
        )
        await ctx.send(embed=emb)

    @commands.command(aliases=['gayrate', 'GAYRATE'])
    async def gay_scanner(self, ctx, *, user: discord.Member):
        """very mature command yes haha"""
        if not user:
            user = ctx.author.name
        gayness = random.randint(0, 100)
        if gayness <= 33:
            gayStatus = random.choice([
                "No homo", "Wearing socks", '"Only sometimes"', "Straight-ish",
                "No homo bro", "Girl-kisser", "Hella straight"
            ])
            gayColor = 0xFF69B4
        elif 33 < gayness < 66:
            gayStatus = random.choice([
                "Possible homo", "My gay-sensor is picking something up",
                "I can't tell if the socks are on or off", "Gay-ish",
                "Looking a bit homo", "lol half  g a y",
                "safely in between for now"
            ])
            gayColor = 0xFF69B4
        else:
            gayStatus = random.choice([
                "LOL YOU GAY XDDD FUNNY", "HOMO ALERT",
                "MY GAY-SENSOR IS OFF THE CHARTS", "STINKY GAY", "BIG GEAY",
                "THE SOCKS ARE OFF", "HELLA GAY"
            ])
            gayColor = 0xFF69B4
        emb = discord.Embed(description=f"Gayness for **{user}**",
                            color=gayColor)
        emb.add_field(name="Gayness:", value=f"{gayness}% gay")
        emb.add_field(name="Comment:", value=f"{gayStatus} :kiss_mm:")
        emb.set_author(
            name="Gay-Scanner™",
            icon_url=
            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png"
        )
        await ctx.send(embed=emb)

    @Eightball.error
    async def Eightball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Wait a minute!",
                                  description="You forgot to ask the question",
                                  color=0xb9b9b9)
            await ctx.send(embed=embed)

    @commands.command(name="coinflip")
    async def flip(self, ctx):
        Heads_Or_Tails = ['heads', 'tails']

        await ctx.send(random.choice(Heads_Or_Tails))

    @commands.command(aliases=['MEME', 'Meme', 'mEmE'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as a:
            async with a.get("https://some-random-api.ml/meme") as b:
                c = await b.json()

                Meme_Phrases = [
                    'Heres  a Juicy meme!', 'Dank meme', 'meememeemem',
                    'A naisu meme', 'funny inn"it', 'A funny meme', 'LOOOL',
                    ':rofl:'
                ]
                embed = discord.Embed(title=random.choice(Meme_Phrases),
                                      description="",
                                      color=0xb9b9b9)

                embed.set_image(
                    url=c['image'])  #ok so just gonna do something here
                await ctx.send(embed=embed)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title='Slow down!',
                                  description='this command is on cooldown',
                                  color=0xb9b9b9)
            await ctx.send(embed=embed)

    @commands.command(aliases=['pp', 'PP'], help="rates pp size")
    async def Pp(self, ctx, arg1):

        Pp_Phrases = [
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8=D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8==D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8===D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8====D ',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8=====D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8======D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8=======D ',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8========D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8=========D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8==========D ',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8===========D',
            f'***PEEPEE SIZE MACHINE*** \n{arg1}s peepee \n 8============D',
        ]
        await ctx.send(random.choice(Pp_Phrases))

    @Pp.error
    async def Pp_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Wait a minute!",
                description="You forgot to mention someone to rate",
                color=0xb9b9b9)
            await ctx.send(embed=embed)

    
    @commands.command(aliases=['iq', 'IQ'])
    async def Iq(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        msg = await ctx.send(":thinking_face:")
        embed = discord.Embed(title=":brain: IQ Test")
        embed.set_author(name=str(user), icon_url=ctx.author.avatar_url)

        iqrange = random.randint(0, 10)
        rate = random.randint(0, 50) * iqrange

        if random.randint(0, 100) == random.randint(0, 100):
            embed.description = "{}\n\n**INFINITY!** {} is so smart that I can't even calculate it!".format(
                str(user))
        else:
            embed.description = r"**{}**'s IQ is **{}**!".format(
                str(user), str(rate))

        embed.color = 0xb9b9b9
        await msg.edit(embed=embed)

    @commands.command(help="Shows a random quote.",
                      description="This command takes no arguments",
                      brief='/utility/misc',
                      aliases=['quote', 'QUOTE'])
    async def Quote(self, ctx):
        async with ctx.typing():
            async with aiohttp.ClientSession() as session:
                response = await session.get("https://zenquotes.io/api/random")
                json_data = json.loads(await response.text())
                quote = json_data[0]['q'] + " -" + json_data[0]['a']

            await ctx.send(quote)

    @commands.command(aliases=['roast', 'ROAST'])
    async def Roast(self, ctx):
        async with ctx.typing():
            response = requests.get(
                url=
                "https://evilinsult.com/generate_insult.php?lang=en&type=json")
            roast = json.loads(response.text)
            await ctx.send(roast['insult'])

    @commands.command(aliases=["fact", "FACT"])
    async def Fact(self, ctx):
        id = random.randint(0, 1490)
        complete_url = 'http://www.randomfactgenerator.net/?id=' + str(id)

        if id == 1490:
            await ctx.send('Facts don\'t care about your feelings!')
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(complete_url) as response:
                    if response.status != 200:
                        return await ctx.send('No fact found :(')

                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    fact = soup.find(id='z')
                    # print(fact.text.split('\n')[0])

                    embed = discord.Embed(color=0xb9b9b9,
                                          timestamp=ctx.message.created_at)
                    embed.add_field(name=f'Fact #{id}:',
                                    value=fact.text.split('\n')[0])
                    await ctx.send(embed=embed)

  




  
    @commands.command(aliases=['gym-tips', 'GYM-TIPS'], help="sends a gym tip")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Gymtips(
        self,
        ctx,
    ):
        async with ctx.typing():

            Gym_Phrases = [
                '``Be Sure to Get Sleep, REST = GAINS``',
                '``Keep Track of Calories/protein intake Per Day``',
                '``prioritise form over heavy weights``',
                '``if you are working for muscle, workout to failure or close to``',
                '``Dont compare yourself to people who are further along in their fitness journey``',
                '``set realistic goals``',
                '``take progress pics, they can be motivation to keep going once you see your progress over time``',
                '``make sure you drink A LOT of water``',
                '``dont be that guy who hogs all the dumbells/plates``',
                '``listen to music while working out it can help with motivation``',
                '``MANY will be too self-focused to even notice what you look like``'
            ]

            await ctx.send(random.choice(Gym_Phrases))

    @Gymtips.error
    async def Problem_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title='Slow down!',
                                  description='this command is on cooldown',
                                  color=0xb9b9b9)
            await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['FACEREVEAL', 'FaceReveal'])
    async def facereveal(self, ctx, arg1):

        Face_reveal_phrases = [
            f"{arg1}'s face got EXPOSED by {ctx.author}",
            f"{ctx.author} finally REVEALED {arg1}'s Ugly face",
            f"{ctx.author} removed {arg1}'s mask off!!!"
        ]

        face_photos = [
        'https://cdn.discordapp.com/attachments/911613120202551306/912011795785470002/unknown.png',
        'https://cdn.discordapp.com/attachments/911613120202551306/912011855420092446/unknown.png',
        'https://cdn.discordapp.com/attachments/911613120202551306/912011876395806791/unknown.png',
        'https://cdn.discordapp.com/attachments/911613120202551306/912012091492302868/unknown.png',
        'https://cdn.discordapp.com/attachments/911613120202551306/912012259990052965/unknown.png',
        'https://cdn.discordapp.com/attachments/911613120202551306/912012326041964634/unknown.png'
        ]
        embed = discord.Embed(title='',
                              description=random.choice(Face_reveal_phrases),
                              color=0xb9b9b9)
        embed.set_image(url=random.choice(face_photos))
        embed.set_footer(text='Exposed lulw')
        await ctx.send(embed=embed)

       


def setup(client):
    client.add_cog(fun(client))
