
import discord
from discord import Member
from typing import Optional
from discord.ext import commands
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('/home/runner/Sewayaki-bot-no-Aruya-chan/cfg.ini')

class info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name = "userinfo", aliases = ["memberinfo", "ui", "mi"])
  async def user_info(self, ctx, target: Optional[Member]):
    """shows information about specyfic user\nif target not passed target = author"""
    target = target or ctx.author

    embed = discord.Embed(title = "Uesr information", colour = target.colour)

    embed.set_thumbnail(url = target.avatar_url)

    #embed.set_footer(text = target.avatar_url)

    embed.add_field(name = "ID", value = target.id, inline = False)
    embed.add_field(name = "Name", value = str(target), inline = True)
    embed.add_field(name = "Top role", value = target.top_role.mention, inline = True)
    embed.add_field(name = "Is a bot", value = target.bot, inline = True)
    embed.add_field(name = "Status", value = target.raw_status, inline = True)
    embed.add_field(name = "Created at", value = target.created_at.strftime('%d.%m.%Y %H:%M:%S'), inline = True)
    embed.add_field(name = "Joined at", value = target.joined_at.strftime('%d.%m.%Y %H:%M:%S'), inline = True)

    await ctx.send(embed = embed)

  @commands.command(name = "uesrroles", aliases = ["ur"])
  async def uesr_roles(self, ctx, target: Optional[Member]):
    target = target or ctx.author

    embed = discord.Embed(title = str(target) + "'s" + "  roles ", colour = target.colour)

    embed.set_thumbnail(url = target.avatar_url)

    embed.add_field(name = "Top role", value = target.top_role.mention, inline = False)

    n = 0
    for role in target.roles:
      n = n + 1
      embed.add_field(name = str(n) + ".", value = str(role), inline = False)

    await ctx.send(embed = embed)

  @commands.command(name = "guildroles", aliases = ["gr", "serverroles", "sr"])
  async def guild_roles(self, ctx):

    embed = discord.Embed(title = "Guild  roles:", colour = cfg.getint('general', 'bot_colour'))

    embed.set_thumbnail(url = ctx.guild.icon_url)

    embed.set_author(name = f"There are {len(ctx.guild.roles)} roles in the {ctx.guild.name} server")

    n = 0
    for role in ctx.guild.roles:
      n = n + 1
      embed.add_field(name = str(n) + ".", value = str(role), inline = False)

    await ctx.send(embed = embed)

  @commands.command(name = "guildinfo", aliases = ["gi", "serverinfo", "si"])
  async def guild_info(self, ctx):
    embed = discord.Embed(title = "Server information", colour = cfg.getint('general', 'bot_colour'))

    embed.set_thumbnail(url = ctx.guild.icon_url)

    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

    embed.add_field(name = "Name", value = ctx.guild.name, inline = False)
    embed.add_field(name = "ID", value = ctx.guild.id, inline = False)
    embed.add_field(name = "Owner", value = ctx.guild.owner, inline = True)
    embed.add_field(name = "Created at", value = ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline = False)
    embed.add_field(name = "How many ppl", value = len(list(filter(lambda m: not m.bot, ctx.guild.members))), inline = False)
    embed.add_field(name = "How many bots", value = len(list(filter(lambda m: m.bot, ctx.guild.members))), inline = True)
    embed.add_field(name = "Statuses", value = f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚫ {statuses[3]}", inline = False)
    embed.add_field(name = "How many txt channels", value = len(ctx.guild.text_channels), inline = False)
    embed.add_field(name = "How many voice channels", value = len(ctx.guild.voice_channels), inline = True)

    """
    n = str(ctx.guild.by_category())

    embed.add_field(name = "Channels", value = n, inline = False)

    for categories in ctx.guild.categories:
      n = ""
      for channels in ctx.guild.channels:
        n = n + "\n " + str(channels)
      embed.add_field(name = categories, value = n, inline = True)
    """

    await ctx.send(embed = embed)

def setup(client):
  client.add_cog(info(client))

