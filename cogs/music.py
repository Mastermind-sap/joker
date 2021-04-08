import discord
from discord.ext import commands,tasks
from pytube import YouTube
import random
import requests
import json
import asyncio
import itertools


async def music_commands(ctx):
    await ctx.send(ctx.author.mention+" all the music commands are only for educational purposes")
    await ctx.send("Music commands are AGAINST YOUTUBE POLICIES, hence restricted :negative_squared_cross_mark: ")
    return False

class Music(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    ## MUSIC COMMANDS
    ## AGAINST YOUTUBE POLICIES
    ## ONLY FOR EDUCATIONAL PURPOSES
    ## Youtube doesnot allow downloading its videos
    ## DOESNOT work from heroku server as the download doesnot take place
    ## ONLY FUNCTIONAL FROM PERSONAL COMPUTER (as of i know)
            
    @commands.check(music_commands)
    @commands.command(aliases=["p"])
    async def play(self,ctx,*,query):
        try:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=str(ctx.message.author.voice.channel))
            await voiceChannel.connect()
            await ctx.send("Joined "+str(ctx.message.author.voice.channel)+" voice channel!:white_check_mark:")
        except AttributeError:
            await ctx.send(ctx.message.author.mention+" is not in any voice channel :negative_squared_cross_mark:")
            return
        except Exception as e:
            print(e)
        
        url=None
        if len(query)==0:
            await ctx.send(ctx.message.author.mention+"you need to provide a youtube video link or any query with the play command :negative_squared_cross_mark:")
            return
        elif query.startswith("https://www.youtube.com/watch?v="):
            url=query
        else:
            s=gs.search("https://www.youtube.com/results?search_query="+query.replace(" ","+"),"com","en",num=10,stop=10,pause=2.0)
            for i in s:
                if i.startswith("https://www.youtube.com/watch?v="):
                    url=i
                    break
        if url==None:
            await ctx.send(ctx.message.author.mention+" some error is caused :negative_squared_cross_mark:")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        yt=YouTube(str(url))
        yt_embed=discord.Embed(title=yt.title+":musical_note:",description=yt.description,color=discord.Colour.red())
        yt_embed.set_thumbnail(url=yt.thumbnail_url)
        yt_embed.add_field(name="Author: ",value=yt.author+":musical_score: ",inline=False)
        yt_embed.add_field(name="Duration: ",value=str(yt.length)+" seconds :clock3: ",inline=False)
        yt_embed.add_field(name="Publish date: ",value=str(yt.publish_date)+":calendar_spiral:",inline=False)
        yt_embed.add_field(name="Rating: ",value=str(yt.rating)+":star2:",inline=False)
        yt_embed.add_field(name="Views: ",value=str(yt.views)+":eyes:",inline=False)
        t=yt.streams.filter(only_audio=True)
        t[0].download(".\songs")
        try:
            print(".\songs\\"+yt.title+".mp4")
            voice.play(discord.FFmpegPCMAudio(".\songs\\"+yt.title+".mp4"))
            await ctx.send("Playing "+yt.title+" :loud_sound:")
            await ctx.send(embed=yt_embed)
        except Exception as e:
            print(e)
            await ctx.send(ctx.message.author.mention+" joker already playing audio :negative_squared_cross_mark:")
            await ctx.send("Use stop command to stop the currently playing song and leave command to make joker exit the current voice channel")
            return

    @commands.check(music_commands)    
    @commands.command(aliases=["disconnect","exit"])
    async def leave(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.send("Disconnected :wave:")
        else:
            await ctx.send("The bot is not connected to a voice channel. :negative_squared_cross_mark:")

    @commands.check(music_commands)
    @commands.command()
    async def pause(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send("Paused :pause_button:")
        else:
            await ctx.send("Currently no audio is playing. :negative_squared_cross_mark:")

    @commands.check(music_commands)
    @commands.command()
    async def resume(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send("Resumed :play_pause: ")
        else:
            await ctx.send("The audio is not paused. :negative_squared_cross_mark:")

    @commands.check(music_commands)
    @commands.command()
    async def stop(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send("Stopped playing :octagonal_sign: ")






def setup(bot):
    bot.add_cog(Music(bot))
