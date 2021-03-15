import discord
import random
from discord.ext import commands,tasks
from itertools import cycle
import pyjokes
import joke_generator
import requests
import xkcd
import googlesearch as gs
import giphypop as gp
import json
from pytube import YouTube
import akinator as ak
import asyncio
import itertools
import chessdotcom as chess
import randfacts

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!joker ',intents=intents)
bot.remove_command("help")
status=cycle(["Why So Sad!?","JOKER IS HERE","Use !joker"])

@bot.command(pass_context=True)
async def help(ctx):
    author=ctx.message.author

    #main help command
    help_embed=discord.Embed(title="Joker Help",description="Use !joker before any command",color=discord.Colour.red())
    #help_embed.set_thumbnail(url=bot.user.avatar_url)
    help_embed.set_thumbnail(url="https://media.tenor.com/images/b9432c96a5ff07c194f337e7b43ff248/tenor.gif")    
    #help_embed.set_image(url="https://media.tenor.com/images/b9432c96a5ff07c194f337e7b43ff248/tenor.gif")
    help_embed.set_footer(text="Requested by: "+str(author))
    await author.send(embed=help_embed)

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
    await author.send(embed=server_embed)

    #greeting commands
    greet_embed=discord.Embed(title="Greeting commands",description="Use these commands to greet other members",color=discord.Colour.red())
    greet_embed.set_thumbnail(url="https://media.tenor.com/images/1ab4a2bf24e962b03c27a4c8352c3e2f/tenor.gif")
    greet_embed.add_field(name="hi/hello",value="say hi",inline=False)
    greet_embed.add_field(name="uthere/areuthere",value="ask are you there",inline=False)
    greet_embed.add_field(name="goodmorning/gm",value="wish goodmorning",inline=False)
    greet_embed.add_field(name="goodnight/goodn8/nightynight/gn",value="wish goodnight",inline=False)
    greet_embed.add_field(name="bye/sayonara/adios",value="say bye",inline=False)
    await author.send(embed=greet_embed)
    
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
    await author.send(embed=fun_embed)

    #music commands
    music_embed=discord.Embed(title="Music commands",description="Use these commands to play music/youtube audio",color=discord.Colour.red())
    music_embed.set_thumbnail(url="https://media1.tenor.com/images/66e25c15d969c51a9158637959fcec04/tenor.gif?itemid=9872650")
    music_embed.add_field(name="WILL NOT WORK",value="only for educational purposes(against youtube policies)",inline=False)
    music_embed.add_field(name="play/p",value="play some audio from youtube video link or from the given query",inline=False)
    music_embed.add_field(name="leave/disconnect/exit",value="make the bot leave the voice channel",inline=False)
    music_embed.add_field(name="pause",value="pause current music",inline=False)
    music_embed.add_field(name="resume",value="resume current music",inline=False)
    music_embed.add_field(name="stop",value="stop current music",inline=False)
    await author.send(embed=music_embed)
    
    #other utility commands
    utility_embed=discord.Embed(title="Utility commands",description="Some more utility commands",color=discord.Colour.red())
    utility_embed.set_thumbnail(url="https://media.tenor.com/images/d18970558b618156dd0bad57bede8ac1/tenor.gif")
    utility_embed.add_field(name="search",value="search for query and return n number of results (max n=5)",inline=False)
    utility_embed.add_field(name="gif/gifs",value="get a gif according to query you give",inline=False)
    utility_embed.add_field(name="randomgif/randg",value="get a random gif",inline=False)
    utility_embed.add_field(name="quote",value="send a random quote",inline=False)
    utility_embed.add_field(name="randomfact/rfact",value="send a random fact",inline=False)
    await author.send(embed=utility_embed)
    
async def is_it_me(ctx):
    if(str(ctx.author.id) == mainaccid):
        await ctx.send("HELLO MASTERMIND")
        return True
    else:
        await ctx.send("ONLY MASTERMIND(owner of the bot) CAN USE THIS COMMAND")
        return False

async def music_commands(ctx):
    await ctx.send(ctx.author.mention+" all the music commands are only for educational purposes")
    await ctx.send("Music commands are AGAINST YOUTUBE POLICIES, hence restricted :negative_squared_cross_mark: ")
    return False

@bot.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(bot))

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))
    
@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if ('welcome' in channel.name.lower()):
            try:
                welcome=discord.Embed(title=member.name,description=f"""Welcome to {member.guild} {member.mention}""",color=discord.Colour.red())
                welcome.add_field(name="ID",value=member.id,inline=False)
                welcome.set_thumbnail(url=member.avatar_url)
                await channel.send(embed=welcome)
            except Exception as e:
                pass

@bot.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if ('goodbye' in channel.name.lower()):
            try:
                left=discord.Embed(title=member.name,description=f"""{member.mention} left the server""",color=discord.Colour.red())
                left.add_field(name="ID",value=member.id,inline=False)
                left.set_thumbnail(url=member.avatar_url)
                await channel.send(embed=left)
            except Exception as e:
                pass

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments!")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("Invalid command!")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("You are not authorized to use this command!")

@bot.command()
async def mention(ctx, user : discord.Member):
  await ctx.send(user.mention)

@bot.command(aliases=["info","details"])
async def whois(ctx, member : discord.Member = None):
    if not member:
        member = ctx.author
    embed=discord.Embed(title=member.name,description=member.mention,color=discord.Colour.red())
    embed.add_field(name="ID",value=member.id,inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=["getprofilepic","dp"])
async def getdp(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)

@bot.command(aliases=["dm","pvtmessage"])
async def pm(ctx , member: discord.Member = None,*,text):
    if not member:
        member = ctx.author
    await member.send(text)

@bot.command(aliases=["clean"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)

hi_urls=["https://media.tenor.com/images/89875b33e32cdd0d1777553653a6717c/tenor.gif",
    "https://media.tenor.com/images/852dab1b47145c779f3266a9ac76d922/tenor.gif",
    "https://media.tenor.com/images/18e364be2476610c0c760a631c63416e/tenor.gif",
    "https://media.tenor.com/images/fe3e2d08c49445ca807935eba60e5627/tenor.gif",
    "https://media.tenor.com/images/5fbe85446cdfa0c3ce15b1e4ddc58c37/tenor.gif",
    "https://media.tenor.com/images/1ab4a2bf24e962b03c27a4c8352c3e2f/tenor.gif",
    "https://media.tenor.com/images/1ee82bdcacdbc8ec55443a349ac1ef03/tenor.gif",
    "https://media.tenor.com/images/e6afa2be25c23e4c6f82f6e2faeb3400/tenor.gif"]
@bot.command(aliases=["hi"])
async def hello(ctx, member : discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send('Hello! '+member.mention)
    await ctx.send(random.choice(hi_urls))

uthere_urls=["https://media.tenor.com/images/fa2e94e3d890184f667cf9d0a381a213/tenor.gif",
        "https://media.tenor.com/images/e27c3c608e5502accd4853d343be876c/tenor.gif",
        "https://media.tenor.com/images/fae3cdddd0ca0a75b4fee69188d84e67/tenor.gif",
        "https://media.tenor.com/images/fb438267a923f041ab3b8d5ef2c2e2a4/tenor.gif",
        "https://media.tenor.com/images/843febaec8b2476756038d8300b6c861/tenor.gif",
        "https://media.tenor.com/images/8073fab909716c5cbebfdb6bcc86af71/tenor.gif",
        "https://media.tenor.com/images/9ea44380b5ba010d2e40f321da1564a9/tenor.gif"]
@bot.command(aliases=["uthere"])
async def areuthere(ctx, user : discord.Member = None):
    if not user:
        user=ctx.author
    await ctx.send('Are You There? '+user.mention)
    await ctx.send(random.choice(uthere_urls))

insult_urls=["https://media.tenor.com/images/19c50486ee6b472aba2817024c5ee4a5/tenor.gif",
        "https://media.tenor.com/images/2141dce8c8a73632749ede31cb6dd215/tenor.gif",
        "https://media.tenor.com/images/7397ff5d71c043634233a2be91053d8a/tenor.gif",
        "https://media.tenor.com/images/14cf6a44d0bd56f95eab06051c2c8bfd/tenor.gif",
        "https://media.tenor.com/images/256b5c5dc88a7c74f010ee0505d931ee/tenor.gif",
        "https://media.tenor.com/images/bc0fd16a9423fbe24127f8cccf247846/tenor.gif",
        "https://media.tenor.com/images/e8713cf0d9b7fc9d03215c394b8ffa0b/tenor.gif",
        "https://media.tenor.com/images/ba01b4ab2950342c129876164aa2d70d/tenor.gif"]        
@bot.command()
async def insult(ctx, user : discord.Member =None):
    if not user:
        user=ctx.author
    await ctx.send('Insulting'+user.mention)
    await ctx.send(random.choice(insult_urls))

@bot.command(aliases=["destroy"])
async def troll(ctx, user : discord.Member =None):
    if not user:
        user=ctx.author
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=txt"
    st = requests.get(url)
    await ctx.send(str(user.mention)+st.content.decode("utf-8"))

gm_urls=["https://media.tenor.com/images/027da4b11ab91e5c0dffb388a8c6f060/tenor.gif",
    "https://media.tenor.com/images/84a8c2f0a681c3fc7db9b7084122d5a1/tenor.gif",
    "https://media.tenor.com/images/c591a3e438a4249775bf00457b915793/tenor.gif",
    "https://media.tenor.com/images/2890b109fc92eff030d1c24db0d2a761/tenor.gif",
    "https://media.tenor.com/images/5852b06765c604372f640218b4e24b3d/tenor.gif",
    "https://media.tenor.com/images/8e9f35f9648ab4256531dde31de09a9f/tenor.gif",
    "https://media.tenor.com/images/8f4a3f2f406ecccc8f790d63e5c94e3e/tenor.gif"]
@bot.command(aliases=["gm"])
async def goodmorning(ctx, user : discord.Member =None):
    if not user:
        user=ctx.author
    await ctx.send('Good Morning! '+user.mention)
    await ctx.send(random.choice(gm_urls))

gn_urls=["https://media.tenor.com/images/dec42b8d70a58a62cf106ecac1023d60/tenor.gif",
    "https://media.tenor.com/images/ccd68c7c41800fb7090eced436a1bda0/tenor.gif",
    "https://media.tenor.com/images/ef780440dce0fe33dedf9ca205f2ca1c/tenor.gif",
    "https://media.tenor.com/images/106064f0a356423af9e2ac51bef3409a/tenor.gif",
    "https://media.tenor.com/images/819d5eb6ae504c1b94eacdfa13878688/tenor.gif",
    "https://media.tenor.com/images/4a92c3367012116430b31d2315a5b701/tenor.gif",
    "https://media.tenor.com/images/2e89a44860147edcc6349ed3da9c234f/tenor.gif"]
@bot.command(aliases=["goodn8","nightynight","gn"])
async def goodnight(ctx, user : discord.Member =None):
    if not user:
        user=ctx.author
    await ctx.send('Good Night! '+user.mention)
    await ctx.send(random.choice(gn_urls))

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
@bot.command(aliases=["sayonara","adios"])
async def bye(ctx, user : discord.Member =None):
    if not user:
        user=ctx.author
    await ctx.send('Bye! '+user.mention)
    await ctx.send(random.choice(bye_urls))

@bot.command()
@commands.has_permissions(administrator=True)
async def spam(ctx, times,*,text):
    if int(times)>20:
        times=20
        await ctx.send(ctx.author.mention+" sorry but spam command is limited to 20")
    for i in range(int(times)):
        await ctx.send(text)

@bot.command(aliases=["choose","select","random"])
async def choice(ctx,options="yes ,no"):
    await ctx.send(random.choice(options.split(",")))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency *1000)}ms')
    
@bot.command(aliases=["cjoke"])
async def coding_joke(ctx):
    await ctx.send(pyjokes.get_joke())

@bot.command()
async def joke(ctx):
    await ctx.send(joke_generator.generate())

@bot.command(aliases=["memify"])
async def meme(ctx, user : discord.Member =None):
    if not user:
        user=ctx.author
    await ctx.send("Here's your meme "+user.mention)
    text=random.randint(0,1000000)
    url = f"https://imgflip.com/i/?={text}"
    await ctx.send(url)

##@bot.command()
##async def garfield(ctx, user : discord.Member =None):
##    if not user:
##        user=ctx.author
##    await ctx.send("Here's your garfield comic strip "+user.mention)
##    url = "https://www.bgreco.net/garfield/"
##    r=requests.get(url)
##    await ctx.send(r.content.decode("utf-8"))

@bot.command(aliases=["xkcd"])
async def comic(ctx, user : discord.Member =None):
    async with ctx.typing():
        if not user:
            user=ctx.author
        await ctx.send("Here's your comic "+user.mention)
        url = xkcd.Comic.getImageLink(xkcd.getRandomComic())
        await ctx.send(url)

@bot.command()
async def search(ctx,times=1,*,query):
    async with ctx.typing():
        if times>5:
            times=5
        s=gs.search(query,"com","en",num=times,stop=times,pause=2.0)
        for i in s:
            await ctx.send(i)

@bot.command()
async def server(ctx):
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

@bot.command(aliases=["gifs"])
async def gif(ctx,*,query):
    async with ctx.typing():
        img=gp.translate(query)
        await ctx.send(img.media_url)
        

@bot.command(aliases=["randg"])
async def randomgif(ctx):
    async with ctx.typing():
        a=gp.Giphy()
        b=a.random_gif()
        await ctx.send(b.url)

@bot.command()
@commands.has_permissions(administrator=True)
async def newrole(ctx, *, rolename=None):
    if not rolename:
        await ctx.send("You forgot to provide a name!")
    else:
        role = await ctx.guild.create_role(name=rolename, mentionable=True)
        await ctx.author.add_roles(role)
        await ctx.send(f"Successfully created and assigned {role.mention}!")

##DONOT USE THIS THEN ANYBODY IN SERVER CAN ASSIGN HIMSELF TO ANYROLE
##@bot.command()
##async def takerole(ctx,*,rolename=None):
##    if not rolename:
##        await ctx.send("You forgot to provide a name!")
##    else:
##        role = discord.utils.get(ctx.author.guild.roles,name=rolename)
##        await ctx.author.add_roles(role)
##        await ctx.send(f"Successfully assigned {ctx.author.mention} to {rolename}!")

@bot.command()
@commands.has_permissions(administrator=True)
async def giverole(ctx,member : discord.Member = None,*,rolename=None):
    if not member:
        member = ctx.author
    if not rolename:
        await ctx.send("You forgot to provide a name of role!")
    else:
        role = discord.utils.get(member.guild.roles,name=rolename)
        await member.add_roles(role)
        await ctx.send(f"Successfully assigned {member.mention} to {rolename}!")

@bot.command()
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(quote)

##DANGEROUS-> "https://stackoverflow.com/questions/34385014/how-do-i-set-the-output-of-exec-to-variable-python"
##BUT RUNNING FROM SERVERS LIKE heroku TILL NOW HAVE NOT SHOWN ANY AFFECT ON THE CODING COMPUTER EVEN WITH OS MODULE CODES
##THE OUTPUT IS : "py"
##eval command->executes any python code and displays output(work in progress)
import io
from contextlib import redirect_stdout
@bot.command(aliases=["eval"])
@commands.check(is_it_me)
async def e(ctx,*,code):
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



## MUSIC COMMANDS
## AGAINST YOUTUBE POLICIES
## ONLY FOR EDUCATIONAL PURPOSES
## Youtube doesnot allow downloading its videos
## DOESNOT work from heroku server as the download doesnot take place
## ONLY FUNCTIONAL FROM PERSONAL COMPUTER (as of i know)
        
@commands.check(music_commands)
@bot.command(aliases=["p"])
async def play(ctx,*,query):
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
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
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
@bot.command(aliases=["disconnect","exit"])
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("Disconnected :wave:")
    else:
        await ctx.send("The bot is not connected to a voice channel. :negative_squared_cross_mark:")

@commands.check(music_commands)
@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Paused :pause_button:")
    else:
        await ctx.send("Currently no audio is playing. :negative_squared_cross_mark:")

@commands.check(music_commands)
@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("Resumed :play_pause: ")
    else:
        await ctx.send("The audio is not paused. :negative_squared_cross_mark:")

@commands.check(music_commands)
@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("Stopped playing :octagonal_sign: ")





@bot.command(aliases=["aki"])
async def akinator(ctx):
    intro=discord.Embed(title="Akinator",description="Hello, "+ctx.author.mention+"I am Akinator!!!",color=discord.Colour.blue())
    intro.set_thumbnail(url="https://en.akinator.com/bundles/elokencesite/images/akinator.png?v93")
    intro.set_footer(text="Think about a real or fictional character. I will try to guess who it is")
    bye=discord.Embed(title="Akinator",description="Bye, "+ctx.author.mention,color=discord.Colour.blue())
    bye.set_footer(text="Akinator left the chat!!")
    bye.set_thumbnail(url="https://i.pinimg.com/originals/28/fc/0b/28fc0b88d8ded3bb8f89cb23b3e9aa7b.png")
    await ctx.send(embed=intro)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b","yes","no","probably","idk","back"]
    try:
        aki = ak.Akinator()
        q = aki.start_game()
        while aki.progression <= 80:
            question=discord.Embed(title="Question",description=q,color=discord.Colour.blue())
            ques=["https://i.imgflip.com/uojn8.jpg","https://ih1.redbubble.net/image.297680471.0027/flat,750x1000,075,f.u1.jpg"]
            question.set_thumbnail(url=ques[random.randint(0,1)])
            question.set_footer(text="Your answer:(y/n/p/idk/b)")
            question_sent=await ctx.send(embed=question)
            try:
                msg = await bot.wait_for("message", check=check , timeout=30)
            except asyncio.TimeoutError:
                await question_sent.delete()
                await ctx.send("Sorry you took too long to respond!(waited for 30sec)")
                await ctx.send(embed=bye)
                return
            await question_sent.delete()
            if msg.content.lower() in ["b","back"]:
                try:
                    q=aki.back()
                except ak.CantGoBackAnyFurther:
                    await ctx.send(e)
                    continue
            else:
                try:
                    q = aki.answer(msg.content.lower())
                except ak.InvalidAnswerError as e:
                    await ctx.send(e)
                    continue
        aki.win()
        answer=discord.Embed(title=aki.first_guess['name'],description=aki.first_guess['description'],color=discord.Colour.blue())
        answer.set_thumbnail(url=aki.first_guess['absolute_picture_path'])
        answer.set_image(url=aki.first_guess['absolute_picture_path'])
        answer.set_footer(text="Was I correct?(y/n)")
        await ctx.send(embed=answer)
        #await ctx.send(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?(y/n)\n{aki.first_guess['absolute_picture_path']}\n\t")
        try:
            correct = await bot.wait_for("message", check=check ,timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 30sec)")
            await ctx.send(embed=bye)
            return
        if correct.content.lower() == "y":
            yes=discord.Embed(title="Yeah!!!",color=discord.Colour.blue())
            yes.set_thumbnail(url="https://i.pinimg.com/originals/ae/aa/d7/aeaad720bd3c42b095c9a6788ac2df9a.png")
            await ctx.send(embed=yes)
        else:
            no=discord.Embed(title="Oh Noooooo!!!",color=discord.Colour.blue())
            no.set_thumbnail(url="https://i.pinimg.com/originals/0a/8c/12/0a8c1218eeaadf5cfe90140e32558e64.png")
            await ctx.send(embed=no)
        await ctx.send(embed=bye)
    except Exception as e:
        await ctx.send(e)


@bot.command()
async def mastermind(ctx):
    await ctx.send("MASTERMIND -THE GUESSING GAME")
    await ctx.send("You will have 8 guesses to guess the four digit number")
    answer=str(random.randrange(1000,9999))
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()
    def check_numbers(guess):
        num_correct=0
        a=list(answer)
        b=list(guess)
        for i in (b):
            if i in (a):
                a.remove(i)
                b.remove(i)
                num_correct+=1
        return num_correct

    def check_position(guess):
        pos_correct=0
        for (i,j) in zip(list(guess),list(answer)):
            if i==j:
                pos_correct+=1
        return pos_correct
    try:
        for i in range(8):
            await ctx.send("Guess: ")
            try:
                guess = await bot.wait_for("message", check=check , timeout=30)
                guess=guess.content
            except asyncio.TimeoutError:
                await ctx.send("Sorry you took too long to respond!(waited for 30sec)")
                await ctx.send("Game cancelled")
                return
            if (guess.isnumeric()) and (int(guess) in range(1000,10000)) and (guess!=answer):
                await ctx.send("You got "+str(check_numbers(guess))+" digits correct")
                await ctx.send("You got "+str(check_position(guess))+" digits in correct position")
            elif (guess==answer):
                await ctx.send("YOU WON! The correct number is indeed "+answer)
                break
            else:
                await ctx.send("Bad guess! The number needs to be 4-digit")
        else:
            await ctx.send("YOU LOOSE! You exhausted all your eight guesses")
            await ctx.send("The correct number is indeed "+answer)

    except Exception as e:
        await ctx.send(e)


data=[['Riddle: What has to be broken before you can use it?', 'Answer: An egg'], ['Riddle: I’m tall when I’m young, and I’m short when I’m old. What am I?', 'Answer: A candle'], ['Riddle: What month of the year has 28 days?', 'Answer: All of them'], ['Riddle: What is full of holes but still holds water?', 'Answer: A sponge'], ['Riddle: What question can you never answer yes to?', 'Answer: Are you asleep yet?'], ['Riddle: What is always in front of you but can’t be seen?', 'Answer: The future'], ['Riddle: There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?', 'Answer: There aren’t any—it’s a one-story house.'], ['Riddle. What can you break, even if you never pick it up or touch it?', 'Answer: A promise'], ['Riddle: What goes up but never comes down?', 'Answer: Your age'], ['Riddle: A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?', 'Answer: He was bald.'], ['Riddle: What gets wet while drying?', 'Answer: A towel'], ['Riddle: What can you keep after giving to someone?', 'Answer: Your word'], ['Riddle: I shave every day, but my beard stays the same. What am I?', 'Answer: A barber'], ['Riddle: You see a boat filled with people, yet there isn’t a single person on board. How is that possible?', 'Answer: All the people on the boat are married.'], ['Riddle: You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first?', 'Answer: The match'], ['Riddle: A man dies of old age on his 25 birthday. How is this possible?', 'Answer: He was born on February 29.'], ['Riddle: I have branches, but no fruit, trunk or leaves. What am I?', 'Answer: A bank'], ['Riddle: What can’t talk but will reply when spoken to?', 'Answer: An echo'], ['Riddle: The more of this there is, the less you see. What is it?', 'Answer: Darkness'], ['Riddles for Kids', '20. Riddle: David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?', 'Answer: David'], ['Riddle: I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?', 'Answer: Your shadow'], ['Riddle: What has many keys but can’t open a single lock?', 'Answer: A piano'], ['Riddle: What can you hold in your left hand but not in your right?', 'Answer: Your right elbow'], ['Riddle: What is black when it’s clean and white when it’s dirty?', 'Answer: A chalkboard'], ['Riddle: What gets bigger when more is taken away?', 'Answer: A hole'], ['Riddle: I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?', 'Answer: Your breath'], ['Riddle: I’m found in socks, scarves and mittens; and often in the paws of playful kittens. What am I?', 'Answer: Yarn'], ['Riddle: Where does today come before yesterday?', 'Answer: The dictionary'], ['Riddle: What invention lets you look right through a wall?', 'Answer: A window'], ['Riddle: If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I?', 'Answer: A secret'], ['Riddle: What can’t be put in a saucepan?', 'Answer: It’s lid'], ['Riddle: What goes up and down but doesn’t move?', 'Answer: A staircase'], ['Riddle: If you’re running in a race and you pass the person in second place, what place are you in?', 'Answer: Second place'], ['Riddle: It belongs to you, but other people use it more than you do. What is it?', 'Answer: Your name'], ['Riddles', '35. Riddle: What has lots of eyes, but can’t see?', 'Answer: A potato'], ['Riddle: What has one eye, but can’t see?', 'Answer: A needle'], ['Riddle: What has many needles, but doesn’t sew?', 'Answer: A Christmas tree'], ['Riddle: What has hands, but can’t clap?', 'Answer: A clock'], ['Riddle: What has legs, but doesn’t walk?', 'Answer: A table'], ['Riddle: What has one head, one foot and four legs?', 'Answer: A bed'], ['Riddle: What can you catch, but not throw?', 'Answer: A cold'], ['Riddle: What kind of band never plays music?', 'Answer: A rubber band'], ['Riddle: What has many teeth, but can’t bite?', 'Answer: A comb'], ['Riddle: What is cut on a table, but is never eaten?', 'Answer: A deck of cards'], ['Riddle: What has words, but never speaks?', 'Answer: A book'], ['Riddle: What runs all around a backyard, yet never moves?', 'Answer: A fence\xa0'], ['Riddle: What can travel all around the world without leaving its corner?', 'Answer: A stamp'], ['Riddle: What has a thumb and four fingers, but is not a hand?', 'Answer: A glove'], ['Riddle: What has a head and a tail but no body?', 'Answer: A coin'], ['Riddle: Where does one wall meet the other wall?', 'Answer: On the corner'], ['Riddle: What building has the most stories?', 'Answer: The library\xa0'], ['Riddle: What tastes better than it smells?', 'Answer: Your tongue'], ['Riddle: What has 13 hearts, but no other organs?', 'Answer: A deck of cards'], ['Riddle: It stalks the countryside with ears that can’t hear. What is it?', 'Answer: Corn'], ['Riddle: What kind of coat is best put on wet?', 'Answer: A coat of paint'], ['Riddle: What has a bottom at the top?', 'Answer: Your legs'], ['Riddle: What has four wheels and flies?', 'Answer: A garbage truck'], ['Riddles', '58. Riddle: I am an odd number. Take away a letter and I become even. What number am I?', 'Answer: Seven'], ['Riddle: If two’s company, and three’s a crowd, what are four and five?', 'Answer:\xa0Nine'], ['Riddle: What three numbers, none of which is zero, give the same result whether they’re added or multiplied?', 'Answer: One, two and three'], ['Riddle: Mary has four daughters, and each of her daughters has a brother. How many children does Mary have?', 'Answer:\xa0Five—each daughter has the same brother.'], ['Riddle: Which is heavier: a ton of bricks or a ton of feathers?', 'Answer: Neither—they both weigh a ton.'], ['Riddle: Three doctors said that Bill was their brother. Bill says he has no brothers. How many brothers does Bill actually have?', 'Answer: None. He has three sisters.'], ['Riddle: Two fathers and two sons are in a car, yet there are only three people in the car. How?', 'Answer: They are a grandfather, father and son.'], ['Riddle: The day before yesterday I was 21, and next year I will be 24. When is my birthday?', 'Answer: December 31; today is January 1.'], ['Riddle: A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?', 'Answer: Three'], ['Riddle: A man describes his daughters, saying, “They are all blonde, but two; all brunette but two; and all redheaded but two.” How many daughters does he have?', 'Answer: Three: A blonde, a brunette and a redhead'], ['Riddle: If there are three apples and you take away two, how many apples do you have?', 'Answer: You have two apples.'], ['Riddle: A girl has as many brothers as sisters, but each brother has only half as many brothers as sisters. How many brothers and sisters are there in the family?', 'Answer: Four sisters and three brothers'], ['Riddles', '70. Riddle: What five-letter word becomes shorter when you add two letters to it?', 'Answer: Short'], ['Riddle: What begins with an "e" and only contains one letter?', 'Answer: An envelope'], ['Riddle: A word I know, six letters it contains, remove one letter\xa0and 12 remains. What is it?', 'Answer: Dozens'], ['Riddle: What would you find in the middle of Toronto?', 'Answer: The letter “o”'], ['Riddle: You see me once in June, twice in November and not at all in May. What am I?', 'Answer: The letter “e”'], ['Riddle: Two in a corner, one in a room, zero in a house, but one in a shelter. What is it?', 'Answer: The letter “r”'], ['s'], ["Riddle: I am the beginning of everything, the end of everywhere. I'm the beginning of eternity, the end of time and space. What am I?", 'Answer: Also the letter “e”'], ['Riddle: What 4-letter word can be written forward, backward or upside down, and can still be read from left to right?', 'Answer: NOON'], ['Riddle: Forward I am heavy, but backward I am not. What am I?', 'Answer: The word “not”'], ['Riddle: What is 3\\/7 chicken, 2\\/3 cat and 2\\/4 goat?', 'Answer: Chicago'], ['Riddle: I am a word of letters three; add two and fewer there will be. What word am I?', 'Answer: Few'], ['Riddle: What word of five letters has one left when two are removed?', 'Answer: Stone'], ['Riddle: What is the end of everything?', 'Answer: The letter “g”'], ['Riddle: What word is pronounced the same if you take away four of its five letters?', 'Answer: Queue'], ['Riddle: I am a word that begins with the letter “i.” If you add the letter “a” to me, I become a new word with a different meaning, but that sounds exactly the same. What word am I?', 'Answer: Isle (add “a” to make “aisle”)'], ['Riddle: What word in the English language does the following: The first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word?', 'Answer: Heroine'], ['Riddles', '86. Riddle: What is so fragile that saying its name breaks it?', 'Answer: Silence.'], ['Riddle: What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?', 'Answer: A river'], ['Riddle: Speaking of rivers, a man calls his dog from the opposite side of the river. The dog crosses the river without getting wet, and without using a bridge or boat. How?', 'Answer: The river was frozen.'], ['Riddle: What can fill a room but takes up no space?', 'Answer: Light'], ['Riddle: If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?', 'Answer: A mirror'], [''], ['Riddle: The more you take, the more you leave behind. What are they?', 'Answer: Footsteps'], ['Riddle: I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?', 'Answer: A key'], ['Riddle: People make me, save me, change me, raise me. What am I?', 'Answer: Money'], ['Riddle: What breaks yet never falls, and what falls yet never breaks?', 'Answer: Day, and night'], ['Riddle: What goes through cities and fields, but never moves?', 'Answer: A road'], ['Riddle: I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?', 'Answer: Fire'], ['Riddle: The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?', 'Answer: A coffin'], ['Riddle: A man looks at a painting in a museum and says, “Brothers and sisters I have none, but that man’s father is my father’s son.” Who is in the painting?', 'Answer: The man’s son'], ['Riddle: With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?', 'Answer: A stapler'], ['Riddle: I have lakes with no water, mountains with no stone and cities with no buildings. What am I?', 'Answer: A map'], ['Riddle: What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?', 'Answer: Nothing']]

@bot.command()
async def riddle(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in answer.lower()
    
    i=random.randint(0,102)
    dataitem=data[i]
    riddle=dataitem[0]
    answer=dataitem[1]
    await ctx.send(riddle)
    try:
        a=await bot.wait_for("message", check=check , timeout=30)
        if a.content.lower()== answer.lower()[8:]:
            await ctx.send("Yes you got the answer right")
            await ctx.send(answer)
        else:
            await ctx.send(answer)
    except asyncio.TimeoutError:
        await ctx.send(answer)


@commands.check(is_it_me)
@bot.command()
async def servers(ctx):
    activeservers = bot.guilds
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
@bot.command()
async def msgservers(ctx,*,text):
    activeservers = bot.guilds
    for guild in activeservers:
        for channel in guild.channels:
            if('general' in channel.name.lower()):
                try:
                    await channel.send(text)
                    await ctx.send("Sent message to Guild: "+guild.name+" Channel: "+channel.name)
                except Exception as e:
                    await ctx.send(e)


@commands.check(is_it_me)
@bot.command()
async def msgserver(ctx):
    def check(msg):
        return msg.author == ctx.author and str(ctx.author.id) == mainaccid and msg.channel == ctx.channel
    await ctx.send("Guild name:")
    try:
        guild = await bot.wait_for("message", check=check , timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
        return
    await ctx.send("Channel name:")
    try:
        channel = await bot.wait_for("message", check=check , timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
        return
    await ctx.send("Message:")
    try:
        msg = await bot.wait_for("message", check=check , timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
        return
    await ctx.send("Times:")
    try:
        times = await bot.wait_for("message", check=check , timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
        return
    activeservers = bot.guilds
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
                    

@bot.command(aliases=["chessprofile"])
async def get_player(ctx,*,username):
    try:
        data = chess.get_player_profile(username).json
        data1=chess.is_player_online(username).json
        data2=chess.get_player_clubs(username).json
        profile=discord.Embed(title=data['username'],description=data['name'],color=discord.Colour.red())
        profile.set_thumbnail(url=data['avatar'])
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

@bot.command(aliases=["leaderboards"])
async def print_leaderboards(ctx):
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
@bot.command(aliases=["stats"])
async def get_player_rating(ctx,*,username):
        await ctx.send("Player Ratings")
        data = chess.get_player_stats(username).json
        categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
        for category in categories:
        	await ctx.send('Category:'+str(category))
        	await ctx.send(f'Current: {data[category]["last"]["rating"]}')
        	await ctx.send(f'Best: {data[category]["best"]["rating"]}')
        	await ctx.send(f'Record: {data[category]["record"]}')

@bot.command()
async def chesspuzzle(ctx):
        await ctx.send("Random Puzzle")
        data = chess.get_random_daily_puzzle().json
        await ctx.send(data['title'])
        await ctx.send(data['image'])
        await ctx.send(data['url'])

@bot.command(aliases=["rfact"])
async def randomfact(ctx):
    await ctx.send(randfacts.getFact())
bot.run(token)
