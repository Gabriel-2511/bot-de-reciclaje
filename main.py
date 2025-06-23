import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Se ha iniciado sesión como {bot.user}')

@bot.command()
async def materiales(ctx):
    print("Pueden reciclarse metales, papeles, plásticos y vidrios en sus respectivos contenedores. También pueden ser reciclados algunos equipos electrónicos en puntos limpios.")

@bot.command()
async def contenedores(ctx):
    print("En el contenedor azul van papeles y cartones, en el café van residuos orgánicos, en el gris deben ir desechos no reciclables, en el verde se echa el vidrio, y en el amarillo van plásticos, latas y envases de cartón para líquidos (bricks).")

bot.run("Token")
