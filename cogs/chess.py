import discord
from discord.ext import commands,tasks
import chessdotcom as chess
import random
import requests
import json
import asyncio
import itertools


class Chess(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

                        

    @commands.command(aliases=["chessprofile"])
    async def get_player(self,ctx,*,username):
        try:
            data = chess.get_player_profile(username).json
            data1=chess.is_player_online(username).json
            data2=chess.get_player_clubs(username).json
            profile=discord.Embed(title=data['username'],description=data['name'] if 'name' in data else "No name given",color=discord.Colour.red())
            profile.set_thumbnail(url=data['avatar'] if 'avatar' in data else "https://betacssjs.chesscomfiles.com/bundles/web/images/noavatar_l.1c5172d5.gif")
            profile.add_field(name="Country:",value=data['country'],inline=False)
            profile.add_field(name="Followers:",value=data['followers'],inline=False)
            profile.add_field(name="Status:",value=data['status'],inline=False)
            profile.add_field(name="Online:",value="Yes" if data1['online'] else "No",inline=False)
            profile.add_field(name="Url:",value=data['url'],inline=False)
            for i in data2['clubs']:
                profile.add_field(name="Club:",value=i['name'],inline=False)
            await ctx.send(embed=profile)
        except Exception as e:
            print(e)
            await ctx.send("Username doesnot exist")

    @commands.command(aliases=["leaderboards"])
    async def print_leaderboards(self,ctx):
            await ctx.send("Leaderboards")
            data = chess.get_leaderboards().json
            categories = data.keys()
            for category in categories:
                    await ctx.send('Category:'+str(category))
                    for idx, entry in enumerate(data[category]):
                        if idx<3:
                            await ctx.send(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')
                        else:
                            break
    @commands.command(aliases=["stats"])
    async def get_player_rating(self,ctx,*,username):
            await ctx.send("Player Ratings")
            data = chess.get_player_stats(username).json
            categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
            for category in categories:
                    await ctx.send('Category:'+str(category))
                    await ctx.send(f'Current: {data[category]["last"]["rating"]}')
                    await ctx.send(f'Best: {data[category]["best"]["rating"]}')
                    await ctx.send(f'Record: {data[category]["record"]}')

    @commands.command()
    async def chesspuzzle(self,ctx):
            await ctx.send("Random Puzzle")
            data = chess.get_random_daily_puzzle().json
            await ctx.send(data['title'])
            await ctx.send(data['image'])
            await ctx.send(data['url'])



def setup(bot):
    bot.add_cog(Chess(bot))
