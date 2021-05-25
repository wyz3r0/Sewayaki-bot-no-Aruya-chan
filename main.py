
import discord
import os
from discord.ext import commands
from keep_me_alive import keep_me_alive
from configparser import ConfigParser

intents = discord.Intents.all()

cfg = ConfigParser()
cfg.read('/home/runner/Sewayaki-bot-no-Aruya-chan/cfg.ini')

client = commands.Bot(command_prefix = cfg.get('general', 'bot_prefix'), intents = intents)

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
  if extension == "all":
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        try:
          client.unload_extension(f'cogs.{filename[:-3]}')
          try:
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f' >> {filename[:-3]} successfully reloaded <<')
            await ctx.send(f'> {filename[:-3]} successfully reloaded')
          except commands.ExtensionAlreadyLoaded:
            print(f' >> RELOADING ERROR: cogs.{filename[:-3]} is already loaded <<')
            await ctx.send(f'> cogs.{filename[:-3]} is already loaded')
          except commands.ExtensionNotFound:
            print(f' >> RELOADING ERROR: cogs.{filename[:-3]} not found <<')
            await ctx.send(f'> cogs.{filename[:-3]} not found')
          except commands.ExtensionFailed:
            print(f' >> RELOADING ERROR: cogs.{filename[:-3]} is invalid <<')
            await ctx.send(f'> cogs.{filename[:-3]} is invalid')
        except commands.ExtensionNotFound:
          print(f' >> RELOADING ERROR: cogs.{filename[:-3]} not found <<')
          await ctx.send(f'> cogs.{filename[:-3]} not found')
        except commands.ExtensionError:
          print(f' >> RELOADING ERROR: cogs.{filename[:-3]} is invalid <<')
          await ctx.send(f'> cogs.{filename[:-3]} is invalid')
  else:
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
