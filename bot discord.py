import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def cat(ctx, cat):
    await ctx.send(f"{cat} Has appeared!")
    
@bot.command()
async def bye(ctx):
    await ctx.send(f"adios! - {bot.user} 2025 QUOTE")

bot.run("NO LO VOY A PONER")