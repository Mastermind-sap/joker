import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools


mainaccid=open("mainaccid.txt", "r").read()
async def is_it_me(ctx):
    if(str(ctx.author.id) == mainaccid):
        await ctx.send("HELLO MASTERMIND")
        return True
    else:
        await ctx.send("ONLY MASTERMIND(owner of the bot) CAN USE THIS COMMAND")
        return False

class Restricted(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    ##DANGEROUS-> "https://stackoverflow.com/questions/34385014/how-do-i-set-the-output-of-exec-to-variable-python"
    ##BUT RUNNING FROM SERVERS LIKE heroku TILL NOW HAVE NOT SHOWN ANY AFFECT ON THE CODING COMPUTER EVEN WITH OS MODULE CODES
    ##THE OUTPUT IS : "py"
    ##eval command->executes any python code and displays output(work in progress)
    import io
    from contextlib import redirect_stdout
    @commands.command(aliases=["eval"])
    @commands.check(is_it_me)
    async def e(self,ctx,*,code):
        if code.startswith("```python\n"):
            code=code[9:-3]
        elif code.startswith("```py\n"):
            code=code[5:-3]
        restrictions=["import os","import pyautogui","import sys","import cv2","from os","from pyautogui","from sys","from cv2"]    
        if not any(restriction in code for restriction in restrictions):
            try:
                stdout = io.StringIO()
                with redirect_stdout(stdout):
                    exec(compile(code,'mulstring', 'exec'))
                out = stdout.getvalue()
                await ctx.send("```py\n"+out+"```")
            except:
                await ctx.send("```py\n Error ```")
        else:
            await ctx.send("```py\n Sorry this code is restricted due to security reasons ```")

    @commands.check(is_it_me)
    @commands.command()
    async def servers(self,ctx):
        activeservers = self.bot.guilds
        for guild in activeservers:
            name=str(guild.name)
            description=str(guild.description)
            owner=str(guild.owner)
            _id = str(guild.id)
            region=str(guild.region)
            memcount=str(guild.member_count)
            icon = str(guild.icon_url)

            embed=discord.Embed(
                    title=name +" Server Information",
                    description=description,
                    color=discord.Color.blue()
                    )
            embed.set_thumbnail(url=icon)
            embed.add_field(name="Owner",value=owner,inline=True)
            embed.add_field(name="Server Id",value=_id,inline=True)
            embed.add_field(name="Region",value=region,inline=True)
            embed.add_field(name="Member Count",value=memcount,inline=True)

            await ctx.send(embed=embed)
            print(guild.name)

    @commands.check(is_it_me)
    @commands.command()
    async def msgservers(self,ctx,*,text):
        activeservers = self.bot.guilds
        for guild in activeservers:
            allowed=[]
            for channel in guild.channels:
                if channel.permissions_for(guild.me).send_messages and channel.permissions_for(guild.me).embed_links:
                    allowed.append(channel)
            if len(allowed) >= 1:
                to_post = allowed[0]
                for channel in allowed:
                    if "general" in channel.name.lower():
                        to_post = channel
                        break
                try:
                    await to_post.send(text)
                    await ctx.send("Sent message to Guild: "+guild.name+" Channel: "+to_post.name)
                except Exception as e:
                    await ctx.send(e)


    @commands.check(is_it_me)
    @commands.command()
    async def msgserver(self,ctx):
        def check(msg):
            return msg.author == ctx.author and str(ctx.author.id) == mainaccid and msg.channel == ctx.channel
        await ctx.send("Guild name:")
        try:
            guild = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        await ctx.send("Channel name:")
        try:
            channel = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        await ctx.send("Message:")
        try:
            msg = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        await ctx.send("Times:")
        try:
            times = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        activeservers = self.bot.guilds
        for g in activeservers:
            if g.name==guild.content:
                for ch in g.channels:
                    if(ch.name == channel.content):
                        for i in range(int(times.content)):
                            try:
                                await ch.send(msg.content)
                                await ctx.send("Sent message")
                            except Exception as e:
                                await ctx.send(e)

def setup(bot):
    bot.add_cog(Restricted(bot))
