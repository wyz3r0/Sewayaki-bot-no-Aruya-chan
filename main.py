
import discord
import os
from discord.ext import commands
from keep_me_alive import keep_me_alive

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
  print('Ohayo gozaimasu~ Aruyadesu')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  print(f'{extension} successfully loaded')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  print(f'{extension} successfully unloaded')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}') 
    print(f'{filename} successfully loaded')

keep_me_alive()
client.run(os.getenv('token'))