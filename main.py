import discord
import os
from discord.ext import commands
from keep_me_alive import keep_me_alive

intents = discord.Intents.all()

client = commands.Bot(command_prefix='>', intents = intents)

@client.event
async def on_ready():
  print('Ohayo gozaimasu~ Aruyadesu')
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      try:
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f' >> {filename} successfully loaded <<')
      except:
        print(f' >> INITIAL LOADING ERROR: {filename} is invalid <<')



@client.command()
async def load(ctx, extension):
  try:
    client.load_extension(f'cogs.{extension}')
    print(f' >> {extension} successfully loaded <<')
    await ctx.send(f'> {extension} successfully loaded')
  except commands.ExtensionAlreadyLoaded:
    print(f' >> LOADING ERROR: cogs.{extension} is already loaded <<')
    await ctx.send(f'> cogs.{extension} is already loaded')
  except commands.ExtensionNotFound:
    print(f' >> LOADING ERROR: cogs.{extension} not found <<')
    await ctx.send(f'> cogs.{extension} not found')
  except commands.ExtensionFailed:
    print(f' >> LOADING ERROR: cogs.{extension} is invalid <<')
    await ctx.send(f'> cogs.{extension} is invalid')

@client.command()
async def unload(ctx, extension):
  try:
    client.unload_extension(f'cogs.{extension}')
    print(f' >> {extension} successfully unloaded <<')
    await ctx.send(f'> {extension} successfully unloaded')
  except commands.ExtensionNotFound:
    print(f' >> UNLOADING ERROR: cogs.{extension} not found <<')
    await ctx.send(f'> cogs.{extension} not found')
  except commands.ExtensionError:
    print(f' >> UNLOADING ERROR: cogs.{extension} is invalid <<')
    await ctx.send(f'> cogs.{extension} is invalid')

@client.command()
async def reload(ctx, extension):
  try:
    client.unload_extension(f'cogs.{extension}')
    try:
      client.load_extension(f'cogs.{extension}')
      print(f' >> {extension} successfully reloaded <<')
      await ctx.send(f'> {extension} successfully reloaded')
    except commands.ExtensionAlreadyLoaded:
      print(f' >> RELOADING ERROR: cogs.{extension} is already loaded <<')
      await ctx.send(f'> cogs.{extension} is already loaded')
    except commands.ExtensionNotFound:
      print(f' >> RELOADING ERROR: cogs.{extension} not found <<')
      await ctx.send(f'> cogs.{extension} not found')
    except commands.ExtensionFailed:
      print(f' >> RELOADING ERROR: cogs.{extension} is invalid <<')
      await ctx.send(f'> cogs.{extension} is invalid')
  except commands.ExtensionNotFound:
    print(f' >> RELOADING ERROR: cogs.{extension} not found <<')
    await ctx.send(f'> cogs.{extension} not found')
  except commands.ExtensionError:
    print(f' >> RELOADING ERROR: cogs.{extension} is invalid <<')
    await ctx.send(f'> cogs.{extension} is invalid')

keep_me_alive()
client.run(os.getenv('token'))
