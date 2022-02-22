import discord
from discord.ext import commands
import datetime
bot = commands.Bot(command_prefix='>', description="this is a helper bot")

@bot.command()
async def sum(ctx, NumOne: float, NumTwo: float):
    await  ctx.send(NumOne + NumTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=ctx, describe="lorem impsum"
    , Timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

#events

@bot.event
async def on_ready():
    print("Bot is ready ")

bot.run('OTQ1NzQ3ODk5MzQ4ODE5OTg5.YhUqXg.TR5sRcr6bkTt4qRJ4RUwvAYQJ7w')