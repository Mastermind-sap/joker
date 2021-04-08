import discord
from discord.ext import commands,tasks
import googlesearch as gs
import giphypop as gp
import randfacts
import random
import requests
import json
import asyncio
import itertools


class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def search(self,ctx,times=1,*,query):
        async with ctx.typing():
            if times>5:
                times=5
            s=gs.search(query,"com","en",num=times,stop=times,pause=2.0)
            for i in s:
                await ctx.send(i)

    @commands.command(aliases=["gifs"])
    async def gif(self,ctx,*,query):
        async with ctx.typing():
            img=gp.translate(query)
            await ctx.send(img.media_url)
            
    @commands.command(aliases=["randg"])
    async def randomgif(self,ctx):
        async with ctx.typing():
            a=gp.Giphy()
            b=a.random_gif()
            await ctx.send(b.url)

    @commands.command()
    async def quote(self,ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)

    @commands.command(aliases=["rfact"])
    async def randomfact(self,ctx):
        await ctx.send(randfacts.getFact())

def setup(bot):
    bot.add_cog(Utility(bot))
