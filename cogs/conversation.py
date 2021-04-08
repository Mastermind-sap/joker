import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools

hi_urls=["https://media.tenor.com/images/89875b33e32cdd0d1777553653a6717c/tenor.gif",
        "https://media.tenor.com/images/852dab1b47145c779f3266a9ac76d922/tenor.gif",
        "https://media.tenor.com/images/18e364be2476610c0c760a631c63416e/tenor.gif",
        "https://media.tenor.com/images/fe3e2d08c49445ca807935eba60e5627/tenor.gif",
        "https://media.tenor.com/images/5fbe85446cdfa0c3ce15b1e4ddc58c37/tenor.gif",
        "https://media.tenor.com/images/1ab4a2bf24e962b03c27a4c8352c3e2f/tenor.gif",
        "https://media.tenor.com/images/1ee82bdcacdbc8ec55443a349ac1ef03/tenor.gif",
        "https://media.tenor.com/images/e6afa2be25c23e4c6f82f6e2faeb3400/tenor.gif"]
uthere_urls=["https://media.tenor.com/images/fa2e94e3d890184f667cf9d0a381a213/tenor.gif",
        "https://media.tenor.com/images/e27c3c608e5502accd4853d343be876c/tenor.gif",
        "https://media.tenor.com/images/fae3cdddd0ca0a75b4fee69188d84e67/tenor.gif",
        "https://media.tenor.com/images/fb438267a923f041ab3b8d5ef2c2e2a4/tenor.gif",
        "https://media.tenor.com/images/843febaec8b2476756038d8300b6c861/tenor.gif",
        "https://media.tenor.com/images/8073fab909716c5cbebfdb6bcc86af71/tenor.gif",
        "https://media.tenor.com/images/9ea44380b5ba010d2e40f321da1564a9/tenor.gif"]
insult_urls=["https://media.tenor.com/images/19c50486ee6b472aba2817024c5ee4a5/tenor.gif",
            "https://media.tenor.com/images/2141dce8c8a73632749ede31cb6dd215/tenor.gif",
            "https://media.tenor.com/images/7397ff5d71c043634233a2be91053d8a/tenor.gif",
            "https://media.tenor.com/images/14cf6a44d0bd56f95eab06051c2c8bfd/tenor.gif",
            "https://media.tenor.com/images/256b5c5dc88a7c74f010ee0505d931ee/tenor.gif",
            "https://media.tenor.com/images/bc0fd16a9423fbe24127f8cccf247846/tenor.gif",
            "https://media.tenor.com/images/e8713cf0d9b7fc9d03215c394b8ffa0b/tenor.gif",
            "https://media.tenor.com/images/ba01b4ab2950342c129876164aa2d70d/tenor.gif"]        
gm_urls=["https://media.tenor.com/images/027da4b11ab91e5c0dffb388a8c6f060/tenor.gif",
        "https://media.tenor.com/images/84a8c2f0a681c3fc7db9b7084122d5a1/tenor.gif",
        "https://media.tenor.com/images/c591a3e438a4249775bf00457b915793/tenor.gif",
        "https://media.tenor.com/images/2890b109fc92eff030d1c24db0d2a761/tenor.gif",
        "https://media.tenor.com/images/5852b06765c604372f640218b4e24b3d/tenor.gif",
        "https://media.tenor.com/images/8e9f35f9648ab4256531dde31de09a9f/tenor.gif",
        "https://media.tenor.com/images/8f4a3f2f406ecccc8f790d63e5c94e3e/tenor.gif"]
gn_urls=["https://media.tenor.com/images/dec42b8d70a58a62cf106ecac1023d60/tenor.gif",
        "https://media.tenor.com/images/ccd68c7c41800fb7090eced436a1bda0/tenor.gif",
        "https://media.tenor.com/images/ef780440dce0fe33dedf9ca205f2ca1c/tenor.gif",
        "https://media.tenor.com/images/106064f0a356423af9e2ac51bef3409a/tenor.gif",
        "https://media.tenor.com/images/819d5eb6ae504c1b94eacdfa13878688/tenor.gif",
        "https://media.tenor.com/images/4a92c3367012116430b31d2315a5b701/tenor.gif",
        "https://media.tenor.com/images/2e89a44860147edcc6349ed3da9c234f/tenor.gif"]
bye_urls=["https://media.tenor.com/images/5becc8db5702cc2f9affea9559f10cd1/tenor.gif",
         "https://media.tenor.com/images/e955f55bab6839ec724531e3bae3303c/tenor.gif",
         "https://media.tenor.com/images/0f5b101d294b217d13b3badb43c38fa0/tenor.gif",
         "https://media.tenor.com/images/217be23d6af58e44d7e0fb48595815bd/tenor.gif",
         "https://media.tenor.com/images/93106f99ea2f7638fa0a49af0dc1bd9c/tenor.gif",
         "https://media.tenor.com/images/80534b478b519f315230d7d1c993a326/tenor.gif",
         "https://media.tenor.com/images/bb2599195ea28683463badc924f01c81/tenor.gif",
         "https://media.tenor.com/images/a13b5ae7e6efa9391c2feacaaeaf5656/tenor.gif",
         "https://media.tenor.com/images/9c6383ca347da05c30cc4dbb986d1ca2/tenor.gif",
         "https://media.tenor.com/images/9b282281b97686e155961a542dc57f87/tenor.gif",
         "https://media.tenor.com/images/a211545ceb0e837aba11287fae0b4dce/tenor.gif"]    
    
    
class Greetings(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(aliases=["hi"])
    async def hello(self,ctx, member : discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.send('Hello! '+member.mention)
        await ctx.send(random.choice(hi_urls))

    @commands.command(aliases=["uthere"])
    async def areuthere(self,ctx, user : discord.Member = None):
        if not user:
            user=ctx.author
        await ctx.send('Are You There? '+user.mention)
        await ctx.send(random.choice(uthere_urls))

    @commands.command()
    async def insult(self,ctx, user : discord.Member =None):
        if not user:
            user=ctx.author
        await ctx.send('Insulting'+user.mention)
        await ctx.send(random.choice(insult_urls))

    @commands.command(aliases=["destroy"])
    async def troll(self,ctx, user : discord.Member =None):
        if not user:
            user=ctx.author
        url = "https://evilinsult.com/generate_insult.php?lang=en&type=txt"
        st = requests.get(url)
        await ctx.send(str(user.mention)+st.content.decode("utf-8"))

    @commands.command(aliases=["gm"])
    async def goodmorning(self,ctx, user : discord.Member =None):
        if not user:
            user=ctx.author
        await ctx.send('Good Morning! '+user.mention)
        await ctx.send(random.choice(gm_urls))

    @commands.command(aliases=["goodn8","nightynight","gn"])
    async def goodnight(self,ctx, user : discord.Member =None):
        if not user:
            user=ctx.author
        await ctx.send('Good Night! '+user.mention)
        await ctx.send(random.choice(gn_urls))

    @commands.command(aliases=["sayonara","adios"])
    async def bye(self,ctx, user : discord.Member =None):
        if not user:
            user=ctx.author
        await ctx.send('Bye! '+user.mention)
        await ctx.send(random.choice(bye_urls))



def setup(bot):
    bot.add_cog(Greetings(bot))
