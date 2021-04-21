import discord
from discord.ext import commands,tasks
import pyjokes
import joke_generator
import xkcd
import random
import requests
import json
import asyncio
import itertools
from PIL import Image
import io
import os


class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(aliases=["choose","select","random"])
    async def choice(self,ctx,options="yes ,no"):
        await ctx.send(random.choice(options.split(",")))

    @commands.command(aliases=["cjoke"])
    async def coding_joke(self,ctx):
        await ctx.send(pyjokes.get_joke())

    @commands.command()
    async def joke(self,ctx):
        await ctx.send(joke_generator.generate())

    @commands.command(aliases=["memify"])
    async def meme(self,ctx, user : discord.Member =None):
        if not user:
            user=ctx.author
        await ctx.send("Here's your meme "+user.mention)
        text=random.randint(0,1000000)
        url = f"https://imgflip.com/i/?={text}"
        await ctx.send(url)

    ##@commands.command()
    ##async def garfield(self,ctx, user : discord.Member =None):
    ##    if not user:
    ##        user=ctx.author
    ##    await ctx.send("Here's your garfield comic strip "+user.mention)
    ##    url = "https://www.bgreco.net/garfield/"
    ##    r=requests.get(url)
    ##    await ctx.send(r.content.decode("utf-8"))

    @commands.command(aliases=["xkcd"])
    async def comic(self,ctx, user : discord.Member =None):
        async with ctx.typing():
            if not user:
                user=ctx.author
            await ctx.send("Here's your comic "+user.mention)
            url = xkcd.Comic.getImageLink(xkcd.getRandomComic())
            await ctx.send(url)

    @commands.command()
    async def slap(self,ctx, user : discord.Member =None):
##        if not user:
##            slapper=str(self.bot.id)
##            person=str(ctx.author.id)
##        else:
##            slapper=str(ctx.author.id)
##            person=str(user.id)
##        await ctx.send(f"https://cdn.discordapp.com/attachments/{slapper}/{person}/slap.png")
        try:
            if not user:
                    user=ctx.author
            await ctx.send("Just slapped :wave: "+user.mention)
            response = requests.get(user.avatar_url)
            image_bytes = io.BytesIO(response.content)
            person = Image.open(image_bytes)
            slap = Image.open(".\cogs\slapping\slap.jpg")
            person_res=person.resize((100,100))
            area=(100,100,200,200)
            slap.paste(person_res, area)
            slap.save(".\\cogs\\slapping\\"+str(user.id)+".jpg")
            with open(".\\cogs\\slapping\\"+str(user.id)+".jpg", 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
            os.remove(".\\cogs\\slapping\\"+str(user.id)+".jpg")
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(Fun(bot))
