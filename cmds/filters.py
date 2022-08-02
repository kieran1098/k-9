import discord
from discord.ext import commands
import random
import asyncio
import aiohttp
import time
from discord.ext import *
import utilities
from discord.ext import *
from urllib.parse import quote_plus
from PIL import Image
import praw
import io
from yarl import URL
import assets
import utilities
import json
import blissops as imageops
from random import sample


class filters(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['Arrest', 'ARREST', 'fbi'])
    async def arrest(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        User_avatar = member.avatar

        Arrest_Titles = [
            'FBI OPEN UP!',
            'Busted!',
            "You've been arrested for dealing drugs in school :(",
            'You have the right to remain silent and anything you say may be used against you in a court of law',
        ]

        embed = discord.Embed(title=random.choice(Arrest_Titles),
                              description='',
                              color=0xb9b9b9)
        embed.set_image(
            url=f'https://some-random-api.ml/canvas/jail?avatar={User_avatar}')

        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['Trigger', 'TRIGGER', 'angry'])
    async def trigger(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        User_avatar = member.avatar

        Trigger_Titles = [
            'U mad?',
            "dude's heated up",
            "Get triggered lol",
            'angri >:(',
        ]

        embed = discord.Embed(title=random.choice(Trigger_Titles),
                              description='Somebody is mad :smirk:',
                              color=0xb9b9b9)
        embed.set_image(
            url=
            f'https://some-random-api.ml/canvas/triggered?avatar={User_avatar}'
        )

        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['Gay', 'GAY', 'lgbtq'])
    async def gay(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        User_avatar = member.avatar

        Gay_titles = [
            'Lmfao',
            f"{member.name} likes men",
            "xD",
            'geiii',
        ]

        embed = discord.Embed(title=random.choice(Gay_titles),
                              description=':flushed:',
                              color=0xb9b9b9)
        embed.set_image(
            url=f'https://some-random-api.ml/canvas/gay?avatar={User_avatar}')

        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def tweet(self, ctx, *, words=None):
        if words is not None:

            async with aiohttp.ClientSession() as a:
                path = "https://some-random-api.ml/canvas/tweet/"
                queries = {
                    "username": f"{ctx.author.name}",
                    "avatar": f"{ctx.author.avatar}",
                    "comment": f"{words}",
                    "displayname": f"{ctx.author.name} "
                }
                url = URL.build(path=path, query=queries)
                async with a.get(path) as b:
                    c = io.BytesIO(await b.read())

                    embed = discord.Embed(
                        title="Tweet",
                        description=f"{ctx.author.name} tweeted:",
                        color=0xb9b9b9)
                    embed.set_image(url=url)
                    await ctx.send(embed=embed)

        elif words is None:
            await ctx.send(
                "Add the text you want in the tweet, and then try again.")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    async def youtube(self, ctx, *, words=None):
        if words is not None:

            async with aiohttp.ClientSession() as a:
                path = "https://some-random-api.ml/canvas/youtube-comment"
                queries = {
                    "username": f"{ctx.author.name}",
                    "avatar": f"{ctx.author.avatar}",
                    "comment": f"{words}",
                }
                url = URL.build(path=path, query=queries)
                async with a.get(path) as b:
                    c = io.BytesIO(await b.read())

                    embed = discord.Embed(
                        title="YouTube comment",
                        description=f"{ctx.author.name} commented:",
                        color=0xb9b9b9)
                    embed.set_image(url=url)
                    await ctx.send(embed=embed)

        elif words is None:
            await ctx.send(
                "Add the text you want in the youtube comment, then try again."
            )

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['Wasted', 'WASTED', 'Die'])
    async def wasted(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        User_avatar = member.avatar

        embed = discord.Embed(
            title=':skull:',
            description=
            f"{member.name} Died cuz he forgot to throw the nade after removing the trigger D:",
            color=0xb9b9b9)
        embed.set_image(
            url=f'https://some-random-api.ml/canvas/wasted?avatar={User_avatar}'
        )

        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['Horny', 'HORNY', 'sus'])
    async def horny(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        User_avatar = member.avatar

        embed = discord.Embed(title=':hushed:',
                              description=f"{member.name} is Susaf",
                              color=0xb9b9b9)
        embed.set_image(
            url=f'https://some-random-api.ml/canvas/horny?avatar={User_avatar}'
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(filters(client))
