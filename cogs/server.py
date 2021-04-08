import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools


class Server(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def mention(self,ctx, user : discord.Member):
      await ctx.send(user.mention)

    @commands.command(aliases=["info","details"])
    async def whois(self,ctx, member : discord.Member = None):
        if not member:
            member = ctx.author
        embed=discord.Embed(title=member.name,description=member.mention,color=discord.Colour.red())
        embed.add_field(name="ID",value=member.id,inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["getprofilepic","dp"])
    async def getdp(self,ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.send(member.avatar_url)

    @commands.command(aliases=["dm","pvtmessage"])
    async def pm(self,ctx , member: discord.Member = None,*,text):
        if not member:
            member = ctx.author
        await member.send(text)

    @commands.command(aliases=["clean"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=1):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def spam(self,ctx, times,*,text):
        if int(times)>20:
            times=20
            await ctx.send(ctx.author.mention+" sorry but spam command is limited to 20")
        for i in range(int(times)):
            await ctx.send(text)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.bot.latency *1000)}ms')
        
    @commands.command()
    async def server(self,ctx):
        name=str(ctx.guild.name)
        description=str(ctx.guild.description)
        owner=str(ctx.guild.owner)
        _id = str(ctx.guild.id)
        region=str(ctx.guild.region)
        memcount=str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)

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

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def newrole(self,ctx, *, rolename=None):
        if not rolename:
            await ctx.send("You forgot to provide a name!")
        else:
            role = await ctx.guild.create_role(name=rolename, mentionable=True)
            await ctx.author.add_roles(role)
            await ctx.send(f"Successfully created and assigned {role.mention}!")


    ##DONOT USE THIS THEN ANYBODY IN SERVER CAN ASSIGN HIMSELF TO ANYROLE
    ##@commands.command()
    ##async def takerole(self,ctx,*,rolename=None):
    ##    if not rolename:
    ##        await ctx.send("You forgot to provide a name!")
    ##    else:
    ##        role = discord.utils.get(ctx.author.guild.roles,name=rolename)
    ##        await ctx.author.add_roles(role)
    ##        await ctx.send(f"Successfully assigned {ctx.author.mention} to {rolename}!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giverole(self,ctx,member : discord.Member = None,*,rolename=None):
        if not member:
            member = ctx.author
        if not rolename:
            await ctx.send("You forgot to provide a name of role!")
        else:
            role = discord.utils.get(member.guild.roles,name=rolename)
            await member.add_roles(role)
            await ctx.send(f"Successfully assigned {member.mention} to {rolename}!")

def setup(bot):
    bot.add_cog(Server(bot))
