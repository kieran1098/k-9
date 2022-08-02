import keep_alive
import flask
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

os.environ['MPLCONFIGDIR'] = '/tmp'

initial_extensions = []

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>>', help_command=None, kick_command=None)
bot.remove_command('help')
bot.remove_command('kick')


@bot.event
async def on_ready():
    activity = discord.Game(name=">>help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        initial_extensions.append("cmds." + filename[:-3])

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extensions in initial_extensions:
        bot.load_extension(extensions)

#start the bot with our token
keep_alive.keep_alive()
bot.run(os.environ['token'])
