import os
import random
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

reciclables = ["PET" ,"Vidrio", "Cristal", "Carton", "Papel"]

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def reciclable(ctx, object):
    if not(object in reciclables):
        await ctx.send(f"{object} no es reciclable, Prueba '$reciclable PET'")
    else:
        await ctx.send(f"{object} si es reciclable")
        
@bot.command()
async def fechas_de(ctx, object):
    fechas = {"PET": "2 a 7 años" ,"Vidrio": "10 a 50 años", "Cristal": "10 a 50 años", "Carton": "8 a 12 meses", "Papel": "1 a 7 años"}
    if not(object in reciclables):
        await ctx.send(f"Todavia no tenemos a {object}, pero pronto estara...")
    else:
        fechadecaducidad = fechas[object]
        await ctx.send(f"La fecha de caducidad de {object} es de {fechadecaducidad}")
        
@bot.command()
async def ideas_con(ctx, object):
    ideas = {"PET": "Llaveros o carpetas de PET" ,"Vidrio": "Decoraciones con fundir (no hagan esto en casa niños)", "Cristal": "Decoraciones con fundir (no hagan esto en casa niños)", "Carton": "Jugetes y protectores de platos", "Papel": "Manualidades y origami"}
    if not(object in reciclables):
        await ctx.send(f"Todavia no tenemos a {object}, pero pronto estara como manualidad...")
    else:
        manualidad = ideas[object]
        await ctx.send(f"puedes hacer {manualidad} con {object}")

@bot.command()
async def consejos(ctx):
    consejos = [
        "Apagar las luce cuando no las utilices"
        "No desperdiciar comida"
        "Reciclar basura u organizarla en un contenedor"
        "No tirar basura en la calle"
    ]
    consejo = random.choice(consejos)
    await ctx.send(f"aqui tienes un consejo {consejo}")

bot.run("Token")