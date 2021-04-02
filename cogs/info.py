
import discord
from discord import Member
from typing import Optional
from discord.ext import commands

class info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name = "userinfo", aliases = ["memberinfo", "ui", "mi"])
  async def user_info(self, ctx, target: Optional[Member]):
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

def setup(client):
  client.add_cog(info(client))

