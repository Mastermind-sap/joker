import discord
from discord.ext import commands,tasks
import os
from itertools import cycle
import random
import requests
import json
import asyncio
import itertools

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!joker '),intents=intents)
status=cycle(["Why So Serious!?","JOKER IS HERE","Use !joker or mention me"])

async def is_it_me(ctx):
    if(str(ctx.author.id) == mainaccid):
        await ctx.send("HELLO MASTERMIND")
        return True
    else:
        await ctx.send("ONLY MASTERMIND(owner of the bot) CAN USE THIS COMMAND")
        return False

@bot.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(bot))

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))

# Cogs related functions

@commands.check(is_it_me)
@bot.command()
async def load(ctx,extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded {extension}")
    except Exception as e:
        await ctx.send("Error occured:"+e)
@commands.check(is_it_me)
@bot.command()
async def unload(ctx,extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Unloaded {extension}")
    except Exception as e:
        await ctx.send("Error occured:"+e)

@commands.check(is_it_me)
@bot.command()
async def reload(ctx,extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"Reloaded {extension}")
    except Exception as e:
        await ctx.send("Error occured:"+e)

@commands.check(is_it_me)
@bot.command()
async def loadall(ctx):
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                bot.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"Loaded all")
    except Exception as e:
        await ctx.send("Error occured:"+e)
@commands.check(is_it_me)
@bot.command()
async def unloadall(ctx):
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"Unloaded all")
    except Exception as e:
        await ctx.send("Error occured:"+e)

@commands.check(is_it_me)
@bot.command()
async def reloadall(ctx):
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"cogs.{filename[:-3]}")
                bot.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"Reloaded all")
    except Exception as e:
        await ctx.send("Error occured:"+e)
        
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(token)
