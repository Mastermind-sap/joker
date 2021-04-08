import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools


class Mastermind(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def mastermind(self,ctx):
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
                    guess = await self.bot.wait_for("message", check=check , timeout=30)
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
    

def setup(bot):
    bot.add_cog(Mastermind(bot))
