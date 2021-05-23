
from discord.ext import commands
from configparser import ConfigParser
import default_cfg
import os

cfg = ConfigParser()
cfg.read('/home/runner/Sewayaki-bot-no-Aruya-chan/cfg.ini')

class config(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  def reload(self, extension): #reloading extension/s
    if extension == "all":
      for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
          try:
            self.client.load_extension(f'cogs.{filename[:-3]}')
          except:
            self.client.unload_extension(f'cogs.{filename[:-3]}')
            self.client.load_extension(f'cogs.{filename[:-3]}')
    else:
      try:
        self.client.load_extension(f'cogs.{extension}')
      except:
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')

  @commands.command()
  async def prefix(self, ctx, new_prefix):
    """changes this bot's prefix"""
    pass
  
  @commands.command(name = "colour", aliases = ["color"])
  async def colour(self, ctx, new_colour): #hex to dec
    """changes colour of embeds"""
    try: new_colour = str(new_colour)
    except: pass
    if new_colour == 'default':
      cfg.set('general', 'bot_colour', f"{default_cfg.default_bot_colour}") 
      print(' >> colour changed to default <<')
      await ctx.send('> colour changed to default')
    else:
      old_colour = cfg.getint('general', 'bot_colour')
      cfg.set('general', 'bot_colour', f"{int(new_colour, 16)}")
      print(f" >> colour changed from #{hex(old_colour)[2:]} to #{hex(cfg.getint('general', 'bot_colour'))[2:]} <<")
      await ctx.send(f"> colour changed from #{hex(old_colour)[2:]} to #{hex(cfg.getint('general', 'bot_colour'))[2:]}")

    with open('/home/runner/Sewayaki-bot-no-Aruya-chan/cfg.ini', 'w') as configfile:    # save
      cfg.write(configfile)

    config.reload(self, "all")

    

  @commands.command(name = 'site')
  async def site(self, ctx, site):
    """changes site from which bot is taking images with \">img\" command"""
    old_site = cfg.get('general', 'site')
    cfg.set('general', 'site', f"{site}")
    with open('/home/runner/Sewayaki-bot-no-Aruya-chan/cfg.ini', 'w') as configfile:    # save
      cfg.write(configfile)

    print(f" >> site changed from {old_site} to {site} <<")
    await ctx.send(f"> site changed from {old_site} to {site}")

    config.reload(self, "danbooru")

  @commands.command()
  async def safe_mode(self, ctx, s_m_switch):
    """safe mode is directed to discord servers that do not allow NSFW content
    if this is on no NSFW content and command will be shown by this bot
    if this is off you you will be able to use every command (including NSFW ones) with every avaliable parameter
    
    disclaimer: we do not take any responsibility for un/mistagged images containing NSFW content fetched from third parties"""
    pass

  @commands.command()
  async def emergence(self, ctx, e_switch):
    """MASTER ONLY
    
    this enables the emergence mode
    if this is on only members with master status will be able to interact with this bot
    if this is off all server members can use this bot normally"""
    pass


def setup(client):
  client.add_cog(config(client))
