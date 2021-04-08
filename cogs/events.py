import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools


class Events(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        for channel in member.guild.channels:
            if ('welcome' in channel.name.lower()):
                try:
                    welcome=discord.Embed(title=member.name,description=f"""Welcome to {member.guild} {member.mention}""",color=discord.Colour.red())
                    welcome.add_field(name="ID",value=member.id,inline=False)
                    welcome.set_thumbnail(url=member.avatar_url)
                    await channel.send(embed=welcome)
                except Exception as e:
                    pass

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        for channel in member.guild.channels:
            if ('goodbye' in channel.name.lower()):
                try:
                    left=discord.Embed(title=member.name,description=f"""{member.mention} left the server""",color=discord.Colour.red())
                    left.add_field(name="ID",value=member.id,inline=False)
                    left.set_thumbnail(url=member.avatar_url)
                    await channel.send(embed=left)
                except Exception as e:
                    pass

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass in all required arguments!")
        elif isinstance(error,commands.CommandNotFound):
            await ctx.send("Invalid command!")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send("You are not authorized to use this command!")


def setup(bot):
    bot.add_cog(Events(bot))
