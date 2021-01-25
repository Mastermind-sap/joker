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

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

bot = commands.Bot(command_prefix='!joker ')
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
    server_embed.add_field(name="spam",value="only admins can spam some text n number of times using this command",inline=False)
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
    for channel in member.server.channels:
        if str(channel)=="general":
            await bot.send_message(f"""WELCOME TO THE SERVER {member.mention}""")

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

bot.run(token)
