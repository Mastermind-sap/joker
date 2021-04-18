import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools


class Help(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.bot.remove_command("help")

    @commands.command(pass_context=True)
    async def help(self,ctx):
        
        author=ctx.message.author

        #main help command
        help_embed=discord.Embed(title="Joker Help",description="Use !joker before any command",color=discord.Colour.red())
        #help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        help_embed.set_thumbnail(url="https://media.tenor.com/images/b9432c96a5ff07c194f337e7b43ff248/tenor.gif")    
        #help_embed.set_image(url="https://media.tenor.com/images/b9432c96a5ff07c194f337e7b43ff248/tenor.gif")
        help_embed.set_footer(text="Requested by: "+str(author))
        
        #server commands
        server_embed=discord.Embed(title="Server commands",description="Use these commands to manage the server",color=discord.Colour.red())
        server_embed.set_thumbnail(url="https://media1.tenor.com/images/d69ffe2237924b286e769d081580d2d9/tenor.gif")
        server_embed.add_field(name="mention",value="mentions a user",inline=False)
        server_embed.add_field(name="whois/info/details",value="returns details of mentioned user",inline=False)
        server_embed.add_field(name="getdp/getprofilepic/dp",value="returns the profile pic of mentioned user",inline=False)
        server_embed.add_field(name="pm/dm/pvtmessage",value="sends private message to mentioned user",inline=False)
        server_embed.add_field(name="clean/clear",value="one with managing messages permission can delete n number of msgs from a channel",inline=False)
        server_embed.add_field(name="server",value="get server details",inline=False)
        server_embed.add_field(name="spam",value="only admins can spam some text n(n<=20) number of times using this command",inline=False)
        server_embed.add_field(name="ping",value="display the ping",inline=False)
        server_embed.add_field(name="newrole",value="admin can create a new role",inline=False)
        server_embed.add_field(name="giverole",value="admin can assign any member a role",inline=False)

        #greeting commands
        greet_embed=discord.Embed(title="Greeting commands",description="Use these commands to greet other members",color=discord.Colour.red())
        greet_embed.set_thumbnail(url="https://media.tenor.com/images/1ab4a2bf24e962b03c27a4c8352c3e2f/tenor.gif")
        greet_embed.add_field(name="hi/hello",value="say hi",inline=False)
        greet_embed.add_field(name="uthere/areuthere",value="ask are you there",inline=False)
        greet_embed.add_field(name="goodmorning/gm",value="wish goodmorning",inline=False)
        greet_embed.add_field(name="goodnight/goodn8/nightynight/gn",value="wish goodnight",inline=False)
        greet_embed.add_field(name="bye/sayonara/adios",value="say bye",inline=False)
        
        #fun commands
        fun_embed=discord.Embed(title="Fun commands",description="Use these commands to have a bit of fun",color=discord.Colour.red())
        fun_embed.set_thumbnail(url="https://media1.tenor.com/images/aa51d900b3af7262fda7aa6e8ff024eb/tenor.gif")
        fun_embed.add_field(name="insult",value="insult someone with a gif",inline=False)
        fun_embed.add_field(name="troll/destroy",value="troll someone with a line",inline=False)
        fun_embed.add_field(name="cjoke/coding_joke",value="crack a coding related joke",inline=False)
        fun_embed.add_field(name="joke",value="crack a joke",inline=False)
        fun_embed.add_field(name="meme/memify",value="sends a random meme",inline=False)
        fun_embed.add_field(name="comic/xkcd",value="sends a random comic strip",inline=False)
        fun_embed.add_field(name="choice/choose/select/random",value="choose random item from a list",inline=False)
        fun_embed.add_field(name="akinator/aki",value="Call the akinator",inline=False)
        fun_embed.add_field(name="mastermind",value="Play MASTERMIND -THE GUESSING GAME",inline=False)
        fun_embed.add_field(name="riddle",value="Generate a random riddle from a collection of 101 riddles")
        fun_embed.add_field(name="chessprofile/get_player",value="Get player chess.com profile",inline=False)
        fun_embed.add_field(name="leaderboards/print_leaderboards",value="Get chess leaderboards",inline=False)
        fun_embed.add_field(name="stats/get_player_rating",value="Get player stats",inline=False)
        fun_embed.add_field(name="chesspuzzle",value="Get random chess puzzle",inline=False)

        #music commands
        music_embed=discord.Embed(title="Music commands",description="Use these commands to play music/youtube audio",color=discord.Colour.red())
        music_embed.set_thumbnail(url="https://media1.tenor.com/images/66e25c15d969c51a9158637959fcec04/tenor.gif?itemid=9872650")
        music_embed.add_field(name="WILL NOT WORK",value="only for educational purposes(against youtube policies)",inline=False)
        music_embed.add_field(name="play/p",value="play some audio from youtube video link or from the given query",inline=False)
        music_embed.add_field(name="leave/disconnect/exit",value="make the bot leave the voice channel",inline=False)
        music_embed.add_field(name="pause",value="pause current music",inline=False)
        music_embed.add_field(name="resume",value="resume current music",inline=False)
        music_embed.add_field(name="stop",value="stop current music",inline=False)
        
        #other utility commands
        utility_embed=discord.Embed(title="Utility commands",description="Some more utility commands",color=discord.Colour.red())
        utility_embed.set_thumbnail(url="https://media.tenor.com/images/d18970558b618156dd0bad57bede8ac1/tenor.gif")
        utility_embed.add_field(name="search",value="search for query and return n number of results (max n=5)",inline=False)
        utility_embed.add_field(name="gif/gifs",value="get a gif according to query you give",inline=False)
        utility_embed.add_field(name="randomgif/randg",value="get a random gif",inline=False)
        utility_embed.add_field(name="quote",value="send a random quote",inline=False)
        utility_embed.add_field(name="randomfact/rfact",value="send a random fact",inline=False)
        utility_embed.add_field(name="server_poll",value="creates a poll with only server custom emojis which should be mentioned before poll statement",inline=False)
        utility_embed.add_field(name="poll",value="creates a poll",inline=False)

        def check(reaction, user):
            return user == author and str(reaction.emoji) in ["➡","⬅"]

        help_list=[help_embed,server_embed,greet_embed,fun_embed,music_embed,utility_embed]
        count=0
        help_msg=await ctx.send(embed=help_list[count])
        await help_msg.add_reaction("⬅")
        await help_msg.add_reaction("➡")
        
        while True:
            reaction, user = await self.bot.wait_for('reaction_add',check=check)
            if str(reaction.emoji) == "➡":
                count+=1
                if count>len(help_list)-1:
                    count=0
                await help_msg.edit(embed=help_list[count])
                await help_msg.add_reaction("⬅")
                await help_msg.add_reaction("➡")
        
            elif str(reaction.emoji) == "⬅":
                count-=1
                if count<0:
                    count=len(help_list)-1
                await help_msg.edit(embed=help_list[count])
                await help_msg.add_reaction("⬅")
                await help_msg.add_reaction("➡")

def setup(bot):
    bot.add_cog(Help(bot))

