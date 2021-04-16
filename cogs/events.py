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
    async def on_guild_join(self, guild):
        allowed = []
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages and channel.permissions_for(guild.me).embed_links:
                allowed.append(channel)

        if len(allowed) >= 1:
            to_post = allowed[0]
            for channel in allowed:
                if "general" in channel.name.lower():
                    to_post = channel
                    break
            bot_wel=discord.Embed(title="Joker Bot",description="Hello everyone! Why so serious!",color=discord.Colour.red())
            bot_wel.set_thumbnail(url="https://media.tenor.com/images/b9432c96a5ff07c194f337e7b43ff248/tenor.gif")
            bot_wel.set_author(name=str(guild.me), icon_url=guild.me.avatar_url)
            bot_wel.add_field(name="Use !joker to use my commands", value="You can also mention me "+guild.me.mention+"to use my commands", inline=False)
            bot_wel.add_field(name="Use !joker help", value="To get list of all the commands", inline=False)
            bot_wel.add_field(name=":regional_indicator_d: :regional_indicator_i: :regional_indicator_s: :regional_indicator_c: :regional_indicator_o: :regional_indicator_r: :regional_indicator_d: Official Server:", value="https://discord.gg/jyejPsDgUF", inline=False)
            bot_wel.add_field(name=":regional_indicator_g: :regional_indicator_i: :regional_indicator_t: :regional_indicator_h: :regional_indicator_u: :regional_indicator_b: Discussions:", value="https://github.com/Mastermind-sap/joker/discussions", inline=False)
            bot_wel.set_footer(text="Created by: MASTERMIND")
            await to_post.send(embed=bot_wel)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        for channel in member.guild.text_channels:
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
        for channel in member.guild.text_channels:
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
