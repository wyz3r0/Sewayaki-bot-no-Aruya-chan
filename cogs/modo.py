
import discord
from discord.ext import commands
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('/home/runner/Sewayaki-bot-no-Aruya-chan/cfg.ini')

class modo(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def kick(self, ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'> I kicked {member}\'s ass for: {reason}')

  @commands.command()
  async def ban(self, ctx, member : discord.Member, *, reason = None):
    await member.send(f'Hey {member} you are now in the underworld! If you pray for your soul, my master may forgive your sins. \nList of sins: \n{reason}')
    await member.ban(reason = reason)
    await ctx.send(f'> I smashed {member} with my banhammer for: {reason}')

  @commands.command()
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entery in banned_users:
      user = ban_entery.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'> Woah {user.mention} has been resurected!')
        return

  #@commands.command()
  #async def invite(self, ctx, *, member):
  #  link = ctx.channel.create_invite(max_uses = 1)
  #  ctx.user.id(id)
  #  print(id)

def setup(client):
  client.add_cog(modo(client))
  