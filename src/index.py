import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description="this is a helper bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#events

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Admin"))
    print("Bot is ready ")

bot.run('OTQ1NzQ3ODk5MzQ4ODE5OTg5.YhUqXg.TR5sRcr6bkTt4qRJ4RUwvAYQJ7w')